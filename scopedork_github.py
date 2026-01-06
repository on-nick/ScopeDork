#!/usr/bin/env python3
# GitHub Dork Generator for Bug Hunting
# Prints generated GitHub dorks only

def generate_github_dorks(target):
    dorks = [
        "{target} filename:.esmtprc password",
        "{target} extension:json googleusercontent client_secret",
        "{target} HOMEBREW_GITHUB_API_TOKEN language:shell",
        "{target} xoxp OR xoxb",
        "{target} .mlab.com password",
        "{target} filename:logins.json",
        "{target} filename:CCCam.cfg",
        "{target} msg nickserv identify filename:config",
        "{target} filename:settings.py SECRET_KEY",
        "{target} filename:secrets.yml password",
        "{target} filename:master.key path:config",
        "{target} filename:deployment-config.json",
        "{target} filename:.ftpconfig",
        "{target} filename:.remote-sync.json",
        "{target} filename:sftp.json path:.vscode",
        "{target} filename:sftp-config.json",
        "{target} filename:WebServers.xml",
        "{target} \"api_hash\" \"api_id\"",
        "{target} \"https://hooks.slack.com/services/\"",
        "{target} filename:github-recovery-codes.txt",
        "{target} filename:gitlab-recovery-codes.txt",
        "{target} filename:discord_backup_codes.txt",
        "{target} extension:yaml cloud.redislabs.com",
        "{target} extension:json cloud.redislabs.com",
        "{target} filename:.npmrc _auth",
        "{target} filename:.dockercfg auth",
        "{target} extension:pem private",
        "{target} extension:ppk private",
        "{target} filename:id_rsa OR filename:id_dsa",
        "{target} extension:sql mysql dump",
        "{target} extension:sql mysql dump password",
        "{target} filename:credentials aws_access_key_id",
        "{target} filename:.s3cfg",
        "{target} filename:wp-config.php",
        "{target} filename:.htpasswd",
        "{target} filename:.env DB_USERNAME NOT homestead",
        "{target} filename:.env MAIL_HOST=smtp.gmail.com",
        "{target} filename:.git-credentials",
        "{target} PT_TOKEN language:bash",
        "{target} filename:.bashrc password",
        "{target} filename:.bashrc mailchimp",
        "{target} filename:.bash_profile aws",
        "{target} rds.amazonaws.com password",
        "{target} jsforce extension:js conn.login",
        "{target} SF_USERNAME salesforce",
        "{target} HEROKU_API_KEY language:shell",
        "{target} HEROKU_API_KEY language:json",
        "{target} filename:.netrc password",
        "{target} filename:_netrc password",
        "{target} filename:hub oauth_token",
        "{target} filename:robomongo.json",
        "{target} filename:filezilla.xml Pass",
        "{target} filename:recentservers.xml Pass",
        "{target} filename:config.json auths",
        "{target} filename:connections.xml",
        "{target} filename:.pgpass",
        "{target} filename:proftpdpasswd",
        "{target} filename:server.cfg rcon password",
        "{target} JEKYLL_GITHUB_TOKEN",
        "{target} shodan_api_key language:python",
        "{target} shodan_api_key language:shell",
        "{target} shodan_api_key language:json",
        "{target} shodan_api_key language:ruby",
        "{target} filename:shadow path:etc",
        "{target} filename:passwd path:etc",
        "{target} DATADOG_API_KEY language:shell"
    ]

    print("\n[+] Generated GitHub Dorks:\n")
    for dork in dorks:
        print(dork.replace("{target}", target))


if __name__ == "__main__":
    target = input(
        "Enter GitHub target (example: org:facebook OR user:username OR keyword): "
    ).strip()

    generate_github_dorks(target)
