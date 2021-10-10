# Docker

```
# Docker Command

- docker version
- docker info
- docker container run == docker run
- docker <command> (options)
- docker <command> <sub-command> (options)
- C:\Users\Yuan>docker container run --publish 80:80 nginx
- docker container ls
- docker container stop 690
- docker container ls -a
- docker container rm 690
- docker run --name mongo -d mongo
- docker ps
- docker top mongo
- docker start mongo
- docker logs f8c91284636e
- docker exec <id do container> -ti /bin/bash
```

```
>> docker run -it -p 8888:8888 -v "c:/Users/Yuan/docker_test:/home" continuumio/anaconda3 /bin/bash
                                   => Folder of your computer:Folder of your container
>> (base) root@b385e6ba35f5:/# ls
>> bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
>> (base) root@b385e6ba35f5:/# home
>> bash: home: command not found
>> (base) root@b385e6ba35f5:/# cd /home/
                            ==> Folder of container
>> (base) root@b385e6ba35f5:/home# jupyter notebook --ip='*' --port=8888 --no-browser --allow-root &
>> http://b385e6ba35f5:8888/?token=14a31f116e1aac471fcd9b03390fc3dcf5e937e426cd33af
```
