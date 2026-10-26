import os

os.system("dnf upgrade -y --refresh")
os.system("dnf install -y httpd git")

os.system("systemctl start httpd")
os.system("systemctl enable httpd")

os.system("git clone https://github.com/denilsonbonatti/mundo-invertido.git /tmp/mundo-invertido")
os.system("cp -r /tmp/mundo-invertido/* /var/www/html/")
os.system("rm -rf /tmp/mundo-invertido")

os.system("chown -R apache:apache /var/www/html")
os.system("restorecon -R /var/www/html")
