## Docker primer
```
docker commit -m="added json gem" -a"seanmc" 999529c50741(container name) seanmc/sinatra_image:v1.1

docker run -d ubuntu:latest /bin/bash -c "while :; do echo DockerSeanMc; sleep 1; done"

docker logs <container_name>

docker stop <containename>

docker ps

docker pull
```
### redircect port 8080 locally, 80 on the container
```
docker run -d -p 8080:80 <container name>

docker exec -i -t 08e996ddbd19 ifconfig
```
### create a new image from a container !! like GitHub
```
docker commit 4f4e2bc0bb29(container) centos6:withupdates

docker inspect stoic_brattain | grep IPA
```
### attach to containers shell 
```
docker attach <container>
```
### remove images
```
docker rmi <image>
```
### remove containers
```
docker rm <container>
cat repositories-devicemapper | python -mjson.tool
```
### Dockerfile 
```
FROM centos:centos6.7
MAINTAINER Sean McGuigan <sean.mcguigan@fundingcircle.com>

RUN yum -y update; yum clean all
RUN yum -y install httpd
RUN echo "Docker Test Site" >> /var/www/html/index.html

EXPOSE 80

RUN echo "/sbin/service httpd start" >> /root/.bashrc
```
```
docker build -t seanmc:webserver .(docerfile lives here!!)
docker build —no-cache -f ./loadbalancer -t seanmc:loadbalancer . 
```
### Dockerfile
```
FROM centos:centos6.7
MAINTAINER seanmcguigan <seanmcguigan@gmx.com>

RUN yum -y update; yum clean all
RUN yum -y install httpd
#RUN yum -y install java
#RUN echo "Docker Test Site" >> /var/www/html/index.html

EXPOSE 80

ADD testfile.html /var/www/html/testfile.html

RUN echo "/sbin/service httpd start" >> /root/.bashrc
```
### push to hub
```
docker build -t seanmcguigan/contos6.7:beta1 .
docker push seanmcguigan/centos6.7:beta1(tag)	
```
### clean docker containers images
```
docker rm -v $(docker ps -a -q -f status=exited)
```
### stop all containers
```
docker stop $(docker ps -q)
docker rmi $(docker images -f "dangling=true" -q)
docker run -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker --rm martin/docker-cleanup-volumes
```
### add file during build(in the docker file)
```
ADD testfile.html /var/www/html/testfile.html
```
### add/attach vol
```
docker run -i -t -v /data test:html /bin/bash
```
### map volume(like vagrant)
```
docker run -i -t -v /root/docs:/var/docs test:html /bin/bash
```
### name your container
```
docker run -i -t --name SEANSCONTAINER -d test:html /bin/bash
```
### list all ‘old’ containers
```
docker ps -a
```
### start an old container
```
docker start SEANSCONTAINERv0.1.0
```
### link mounted data across containers
### on one
```
docker run -d -i -t -v /data --name DATA01 seanmc:httpd /bin/bash
```
### on two, will be able to access all volumes mounted on container DATA01
```
docker run -d -i -t —volumes-from DATA01 —name DATA02 seanmc:httpd /bin/bash
```
### commit container changes to new image
```
docker commit your_http_container your_image:http
```
### linking Containers
### setup a container to talk to an existing container
```
docker inspect DATA02|grep IPAdd
        "IPAddress": "172.17.0.9",
        "SecondaryIPAddresses": null,

docker run -i -t --name linked_container --link DATA02:linktarget centos:centos6 /bin/bash
```
### env| less the name of the container it now knows about
```
LINKTARGET_PORT_80_TCP_PROTO=tcp
LINKTARGET_PORT=tcp://172.17.0.9:80
LESSOPEN=||/usr/bin/lesspipe.sh %s
LINKTARGET_PORT_80_TCP_ADDR=172.17.0.9 <—- DATA02 ipaddress 
```
### map random ports on your docker host above 49000 to port 80 within your web server containers.
```
docker run -i -t -d -P seanmc:httpd /bin/bash

6acf86f1774d        seanmc:httpd        "/bin/bash"         7 seconds ago       Up 6 seconds        0.0.0.0:32769->80/tcp   berserk_hoover 
```
### five Useful Docker CLI Commands

### copy from container directory
```
docker cp container_name:/etc/yum.conf /tmp
```
### diff container changes on top of base image 
```
docker diff mywebshit 

C /var
C /var/log
C /var/log/httpd
A /var/log/httpd/error_log
A /var/log/httpd/access_log
C /var/run
C /var/run/httpd
A /var/run/httpd/httpd.pid
C /var/lock
C /var/lock/subsys
A /var/lock/subsys/httpd

C = changed
A = added
D = deleted
```
### system events when creating containers, like tailing logs
```
docker events
```
### view events time window
```
docker events --since 2016-07-07
```
### history of an image
```
docker history seanmcguigan/centos6.7:tomcat6
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
60204d32c705        5 weeks ago         /bin/bash                                       377.7 MB            
23f282322497        5 weeks ago         /bin/sh -c echo "/sbin/service httpd start" >   202 B               
1a4d382db904        5 weeks ago         /bin/sh -c #(nop) EXPOSE 80/tcp                 0 B                 
ee9d95ae4571        5 weeks ago         /bin/sh -c echo "Docker Test Site" >> /var/ww   17 B                
c2da9bac78d6        5 weeks ago         /bin/sh -c yum -y install java                  181.1 MB            
71c2b35a4684        6 weeks ago         /bin/sh -c yum -y install httpd                 115.2 MB            
d7d829c9a59e        6 weeks ago         /bin/sh -c yum -y update; yum clean all         191.7 MB            
c352e3942654        6 weeks ago         /bin/sh -c #(nop) MAINTAINER Sean McGuigan <s   0 B                 
3fba1048142f        8 months ago        /bin/sh -c #(nop) CMD ["/bin/bash"]             0 B                 
b89573a5b116        8 months ago        /bin/sh -c #(nop) LABEL License=GPLv2           0 B                 
8e6730e0eaef        8 months ago        /bin/sh -c #(nop) LABEL Vendor=CentOS           0 B                 
5fc6f5013018        8 months ago        /bin/sh -c #(nop) ADD file:63df1fe23f2f72b766   190.6 MB            
47d44cb6f252        10 months ago       /bin/sh -c #(nop) MAINTAINER The CentOS Proje   0 B         
```
### execute commands inside a running container
### run a container
```
docker run -d -it --name foobar seanmc:java /bin/bash
                           ^          ^
                       container  image used by container
docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
d365ce86e6b8        seanmc:java         "/bin/bash"         7 seconds ago       Up 6 seconds        80/tcp              foobar  

docker exec -it foobar /usr/bin/yum repolist
```
### more commands

### debug info 
```
docker -D info
```
### kill container, pull the plug
```
docker kill my_container
```
### pause a container
```
docker pause my_container
docker unpause my_container
```
### package and export containers
```
docker stop my_container
docker export my_container | gzip > my_container.tgz
```
### import container
```
zcat my_container.tgz | docker import - my_new_image <- lower case
```
### set dns
```
docker run -it --dns=8.8.8.8 --name="mycontainer1" docker.io/ubuntu:latest /bin/bash
docker run -it --dns=8.8.8.8 --dns-search="mydomain.local" --name="mycontainer2" 
docker run -it --dns=8.8.8.8 --dns-search="mydomain.local" --name="mycontainer3" -v /local_vol -v /home/tcox/docker/mydata:/remote_vol docker.io/ubuntu:latest /bin/bash
```

### start services on (boot) start
```
cat ~/.bashrc

# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

/sbin/service httpd start
/sbin/service openssh-server start
```
### create new image for web app
```
docker commit a8564e550bed centos6:baseweb
```
### connect to running container
```
docker exec -it app01 /bin/bash
```
### remove images
docker images ubuntu | tail -n +2 | awk '{ print $1 ":" $2}' | xargs docker rmi

### delete after user
```
docker run --it --rm --name=deleteme-container foo-images /bin/bash
```
