from ape import accounts, project

account = accounts.load("my_account_alias")
account.deploy(project.MyContract)