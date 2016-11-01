FROM geerlingguy/docker-centos7-ansible
RUN yum install -y openssh-server openssh-clients openssh

RUN echo 'root:root' |chpasswd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
