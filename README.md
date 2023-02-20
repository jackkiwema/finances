---
FINANCE
---

* Configure setup according to Vagrantfile
* Install postfix with the below configuration, set it up to use gmail settings

```
sudo apt install postfix mailutils -y --> Internet Site --> $hostname
sudo vi /etc/postfix/sasl/sasl_passwd --> [smtp.gmail.com]:587 user@gmail.com:app_password
sudo postmap /etc/postfix/sasl/sasl_passwd
sudo chown root:root /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db
sudo chmod 0600 /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db
```
* Configure postfix
* `sudo vi /etc/postfix/main.cf`
* Edit `relayhost = [smtp.gmail.com]:587`

* `Append:`
```
smtp_sasl_auth_enable = yes
smtp_sasl_security_options = noanonymous
smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd
smtp_tls_security_level = encrypt
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
```
* `sudo systemctl restart postfix`
* `Test`
```
sendmail $sender_id
To: $Recipient_id
Subject: $Mail Subject
Content: $Mail Content
ctrl d
```

* To deploy updates 
```
git pull
sudo supervisorctl stop finance
flask db upgrade 
sudo supervisorctl start finance
```