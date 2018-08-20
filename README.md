# centos6和centos7的一些区别

#### 1.文件系统
    [CentOS6] ext4
    [CentOS7] xfs
    
>centos7.0开始默认文件系统是xfs，centos6是ext4,
xfs：最大支持8EB（8×1024PB）的单个文件系统
，ext4：的文件系统容量达到1EB，而文件容量则达到16TB
。选择建议：存储海量的小文件，或者超大规模的大文件，建议使用xfs，否则使用ext4，ext4比较稳定，是主流的Linux文件系统，
xfs在大多数场景下整体IOPS表现还是要比ext4来得更高、更稳定，延迟也更小


#### 2.系统内核
    [CentOS6] 2.6.x-x
    [CentOS7] 3.10.x-x
    
>**docker要求内核在3.10以上**



#### 3.防火墙
    [CentOS6] iptables
    [CentOS7] firewalld
    
>    
    
#### 4.文件结构
    [CentOS6] /bin, /sbin, /lib, and /lib64在/下
    [CentOS7] /bin, /sbin, /lib, and /lib64移到/usr下    
    
#### 5.主机名
    [CentOS6] /etc/sysconfig/network
    [CentOS7] /etc/hostname    
> centos7修改主机名：hostnamectl set-hostname HOSTNAME    

#### 6.字符集
>确认是否安装字符集

    [root@localhost ~]$ locale -a |grep en_US
    en_US
    en_US.iso88591
    en_US.iso885915
    en_US.utf8
    
>查看当前字符集

    [root@localhost ~]$ locale
    LANG=en_US.UTF-8
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    ...

>修改当前字符集

    [centos6]
    [root@master ~]$ vim /etc/sysconfig/i18n 
    LANG="en_US.UTF-8"
    SYSFONT="latarcyrheb-sun16"
    [root@master ~]$ source /etc/sysconfig/i18n 

    [centos7]
    #方法1
    [root@localhost ~]$ vi /etc/locale.conf
    # LANG="zh_CN.UTF-8"
    LANG="en_US.UTF-8"
    [root@localhost ~]$ source /etc/locale.conf

    #方法2
    [root@localhost ~]$ localectl set-locale LANG=en_US.UTF-8


#### 7.时区修改
    [CentOS6]
    [root@localhost ~]$ vim /etc/sysconfig/clock
       ZONE="Asia/Chongqing"
    [root@localhost ~]$ ln -s /usr/share/zoneinfo/Asia/Chongqing /etc/localtime

    [CentOS7]
    [root@localhost ~]$ timedatectl set-timezone Asia/Shanghai
    [root@localhost ~]$ timedatectl status



#### 8.服务相关
>centos6:/etc/init.d --> centos7:/usr/lib/systemd，需要自启动运行的程序，一般存在这个系统服务目录下，即：/usr/lib/systemd/system目录，每一个服务以“服务名.service”结尾，该文件的内容一般分为3部分：即[Unit]、[Service]和[Install]。


**1）服务启停**

    [CentOS6]
    service service_name start
    service service_name stop
    service sshd restart/status/reload
    
    [CentOS7]
    systemctl start service_name
    systemctl stop service_name
    systemctl restart/status/reload sshd
    
    
**2）服务开机自启**
   
    [CentOS6]
    chkconfig service_name on/off
    
    [CentOS7]
    systemctl enable service_name
    systemctl disable service_name    
    
    
**3）查看服务**

    [CentOS6]
    chkconfig --list
    
    [CentOS7]
    systemctl list-unit-files
    systemctl --type service    
    
    



>**系统服务举例说明：sshd服务**

    [root@whisky ~]# cat /usr/lib/systemd/system/sshd.service
    [Unit]  #<==对该系统服务描述及说明模块。
    Description=OpenSSH server daemon           #<==描述性说明。
    Documentation=man:sshd(8) man:sshd_config(5)#<==文档列表说明。
    After=network.target sshd-keygen.service    #<==服务依赖类别说明。
    Wants=sshd-keygen.service                   #<==可选的依赖服务。
    
    [Service]   #<==系统服务的运行参数设置模块
    Type=notify #<==服务类型，可选有forking、notify、simple等。
    EnvironmentFile=/etc/sysconfig/sshd  #<==环境变量等的配置文件。
    ExecStart=/usr/sbin/sshd -D $OPTIONS #<==服务的启动程序。
    ExecReload=/bin/kill -HUP $MAINPID   #<==重启程序。
    KillMode=process
    Restart=on-failure
    RestartSec=42s
    
    [Install] #<==服务安装的相关设置。
    WantedBy=multi-user.target   #<==这里为设置多用户级别。可为空格分隔的列表， 表示在使用 systemctl enable 启用此单元时， 将会在对应的目录设置对应文件的软连接。
    更多说明，可参考systemd.unit、system.service文档。
    
>自定义服务：

    [root@whisky ~]# cat /usr/lib/systemd/system/rsyncd_test.service
    [Unit]
    Description=Rsync service
    After=network.target
    
    [Service]
    Type=forking  #<==后台运行。
    PIDFile=/var/run/rsyncd.pid                #<==PID路径。
    ExecStart=/etc/rc.d/init.d/rsyncd start    
    ExecReload=/etc/rc.d/init.d/rsyncd restart 
    ExecStop=/etc/rc.d/init.d/rsyncd stop      
    PrivateTmp=true    #<==开启独立的空间。
    
    [Install]
    WantedBy=multi-user.target  #<==这里为设置多用户级别。
    



**[参考链接:金步国systemd手册](http://www.jinbuguo.com/systemd/systemd.index.html)**
 
