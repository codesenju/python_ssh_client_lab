import paramiko

hostname = 'localhost'
username = 'codesenju'
password = 'passw0rd'
PORT = '2222'
ssh = paramiko.SSHClient()


def execRemoteCommand(cmd, client):
    stdin, stdout, stderr = client.exec_command(cmd)
    output = stderr.readlines()
    for index, item in enumerate(output):
        print(item)
    output = stdout.readlines()
    for index, item in enumerate(output):
        print(item)


try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=password, port=PORT)
    sftp_client = ssh_client.open_sftp()
    cmd = 'ls -l'
    print(cmd)
    execRemoteCommand(cmd, ssh_client)
    sftp_client.put("README.md", "README.md")
    sftp_client.listdir()
    sftp_client.getcwd()
except Exception as err:
    print("SSH CLIENT ERROR: {}".format(err))
finally:
    #    sftp_client.close()
    ssh_client.close()
