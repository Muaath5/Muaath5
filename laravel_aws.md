# Deploy Laravel on AWS Elastic Beanstalk
## Intro
1. Create AWS account
2. Create an application with its environment
3. Create SSH key pair (you will use it to login to console)
4. Select Ubuntu as system
5. Select PHP as language
6. Include the database
7. The root directory should be `/public`
8. Select apache as engine
9. Allow PHP display errors

## Deploy
Zip your files then deploy them:
```bash
sudo php artisan config:clear
sudo zip -r file.zip ./* .env
```

## Login to console
```bash
sudo ssh -i /path/to/key.pem ec2-user@{IP_ADDRESS}
```
Your files will be in `/var/www/html`

## Configuring SSL
### Open port
Go to:
AWS Console > EC2 > Instances > XX > Security > Security groups > Edit inbound rules > Add port 443 for Ipv6, Ipv4

### Apache configuration
First, add your certificate files to `/var/ssl/` in the console.

```bash
cd /etc/httpd/conf.d/elasticbeanstalk
sudo nano php.conf
```
Append:
```
<VirtualHost _default_:443>
    DocumentRoot /var/www/html/public
    ServerName {DOMAIN}
    SSLEngine on
    SSLCertificateFile /var/ssl/file.crt
    SSLCertificateKeyFile /var/ssl/file.key
    SSLCertificateChainFile /var/ssl/file.ca_bundle
</VirtualHost>
```
Then:
```bash
cd /etc/httpd/conf/
sudo nano httpd.conf
```
Append:
```
Listen 443 https
```
Check if it's correct:
```bash
sudo apachectl configtest
```
Then do:
```bash
sudo apachectl restart
```
