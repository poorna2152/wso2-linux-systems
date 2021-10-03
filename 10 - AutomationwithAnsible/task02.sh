ansible lt-server-1-ip -m hostname -a name='lt-2021-031-webserver-1' -i hosts --become
ansible lt-server-2-ip -m hostname -a name='lt-2021-031-webserver-2' -i hosts --become
