# Deploy Laravel on AWS Elastic Beanstalk
## Notes
- In this tutorial, I will use Ubuntu system always
- If it was useful, give it a star

## Intro
1. Create AWS account
2. Create EC2 key pair (you will use it to login to console)
3. Create IAM Instance Profile with permissions
    - AWSElasticBeanstalkWebTier
    - AWSElasticBeanstalkWorkerTier
    - AWSElasticBeanstalkMulticontainerDocker
    - AWSElasticBeanstalkEnhancedHealth
    - AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy
    - AWSElasticBeanstalkRoleWorkerTier
5. Create Elastic Beanstalk application

| Setting          | Value     |
|------------------|-----------|
| System           | Ubuntu    |
| Language         | PHP       |
| EC2 Key Pair     | Yes       |
| Database         | Enabled   |
| Database Policy  | Retain    |
| Root dir         | `/public` |
| Engine           | apache    |
| PHP Errors       | Yes       |

## Manual Deployment
Zip your files then deploy them:
```bash
sudo php artisan config:clear
sudo php artisan optimize:clear
sudo zip ../files.zip -r * .[^.]* -x "vendor/*"
```

## Login to console
```bash
sudo ssh -i /path/to/key.pem ec2-user@{IP_ADDRESS}
```
Your files will be in `/var/www/html` (actually `/var/app/current`)

## Configuring SSL (HTTPS)
### Open port (firewall)
Go to:
AWS Console > EC2 > Instances > {INSTANCE_NAME} > Security > Security groups > Edit inbound rules > Add port 443 for Ipv6, Ipv4

### Apache configuration
First, add your certificate files to some folder (I suggest `/var/ssl/`), then:

```bash
cd /etc/httpd/conf.d/elasticbeanstalk && sudo nano ssl.conf
```
Write:
```
Listen 443 https
<VirtualHost _default_:443>
    DocumentRoot /var/www/html/public
    ServerName {DOMAIN}
    SSLEngine on
    SSLCertificateFile /var/www/html/ssl/file.crt
    SSLCertificateKeyFile /var/www/html/ssl/file.key
    SSLCertificateChainFile /var/www/html/ssl/file.ca-bundle
</VirtualHost>
```
Check if it's correct then restart:
```bash
sudo apachectl configtest && sudo apachectl restart
```

## Auto fetching from GitHub (Not working)
1. Create a pipeline
2. Connect it to your Github account
3. Create CodeBuild, and make everything as default
4. Select Ubuntu as System

And it requires that you have `buildspecs.yml` file on the root, here is a suggested config:
```yml
version: 0.2
phases:
  install:
    commands:
      - echo "##INSTALLING: Composer##"
      - php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
      - php -r "if (hash_file('sha384', 'composer-setup.php') === 'e21205b207c3ff031906575712edab6f13eb0b361f2085f1f1237b7126d785e826a450292b6cfd1d64d92e6563bbde02') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
      - php composer-setup.php
      - php -r "unlink('composer-setup.php');"
  build:
    commands:
      - echo "##Building: START##"
      - composer install
      - composer update
      - php artisan optimize:clear
      - php artisan config:clear
      - php artisan storage:link
      - echo "##Building: END##"
artifacts:
  files:
    - '**/*'
  name: website-$(date +%Y-%m-%d)
```
