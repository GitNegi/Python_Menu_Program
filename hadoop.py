import os

os.system("tput setaf 3")
print("\t\t------->HADOOP CLUSTER<-------")
os.system("tput setaf 7")
print("\n")



def HadoopStart():
    while(True):
        print(

    """
    \t\tPress 0: Exit
    \t\tPress 1: Installing JAVA JDK
    \t\tPress 2: Installing Hadoop Package
    \t\tPress 3: Configure NameNode
    \t\tPress 4: Configure DataNode
    """
)
        choice = int(input("Enter The Choice :-> "))

        if choice == 0:
            break

        if choice == 1:
            loc = input("Enter Software location Incluting Package Name :-> ")
            os.system("rpm -hiv {} ".format(loc))


        if choice == 2:

            loc = input("Enter Software location Including Package Name :-> ")
            os.system("rpm -hiv {} --force".format(loc))


        if choice == 3:
            while True:
                os.system("tput setaf 3")
                print("\t\t --> NameNode <-- ")
                os.system("tput setaf 7")

                print(
                        """
                        \t\tPress 0: EXIT
                        \t\tPress 1: Configure Hdfs file
                        \t\tPress 2: Configure Core file
                        \t\tPress 3: Format File System
                        \t\tPress 4: Start Service
                        \t\tPress 5: Check Service

                        """
                     )
                MNchoice = int(input("Enter Choice :-> "))

                if MNchoice == 0:
                    break

                if MNchoice == 1:
                    fs = open("/etc/hadoop/hdfs-site.xml",'w+')
                    print(fs.write(
                                    """
                                    <?xml version="1.0"?>
                                    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                    <!-- Put site-specific property overrides in this file. -->

                                    <configuration>
                                    <property>
                                    <name>dfs.name.dir</name>
                                    <value>{}</value>
                                    </property>
                                    </configuration>

                                    """.format(input("Enter Folder Name With location "))))

                if MNchoice == 2:
                    fs = open("/etc/hadoop/core-site.xml",'w+')
                    print(fs.write(
                                    """
                                    <?xml version="1.0"?>
                                    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                    <!-- Put site-specific property overrides in this file. -->

                                    <configuration>
                                    <property>
                                    <name>fs.default.name</name>
                                    <value>hdfs://0.0.0.0:{}</value>
                                    </property>
                                    </configuration>

                                    """.format(input(" Enter the Port No :-> "))))

                if MNchoice == 3:
                    os.system("hadoop namenode -format")

                if MNchoice == 4:
                    os.system("hadoop-daemon.sh start namenode")

                if MNchoice == 5:
                    os.system("jps")




        if choice == 4:
            while True:
                os.system("tput setaf 3")
                print("\t\t --> DataNode <-- ")
                os.system("tput setaf 7")

                print(
                        """
                        \t\tPress 0: EXIT
                        \t\tPress 1: Configure Hdfs file
                        \t\tPress 2: Configure Core file
                        \t\tPress 3: Start Service
                        \t\tPress 4: Check Service

                        """
                     )
                dNchoice = int(input("Enter Choice :-> "))

                if dNchoice == 0:
                    break

                if dNchoice == 1:
                    x = input(" Enter Folder Name with location :-> ")
                    os.system("mkdir x")
                    fs = open("hdfs-site.xml",'w+')
                    print(fs.write(
                                    """
                                    <?xml version="1.0"?>
                                    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                    <!-- Put site-specific property overrides in this file. -->

                                    <configuration>
                                    <property>
                                    <name>dfs.data.dir</name>
                                    <value>{}</value>
                                    </property>
                                    </configuration>

                                    """.format(x)))

                if dNchoice == 2:
                    masterip = input("Enter NameNode IP :-> ")
                    masterport = input("Enter Hadoop Service Port NO :-> ")
                    fs = open("/etc/hadoop/core-site.xml",'w+')
                    print(fs.write(
                        """
                        <?xml version="1.0"?>
                        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                        <!-- Put site-specific property overrides in this file. -->

                        <configuration>
                        <property>
                        <name>fs.default.name</name>
                        <value>hdfs://{}:{}</value>
                        </property>
                        </configuration>

                        """.format(masterip,masterport)))



                if dNchoice ==3:
                    os.system("hadoop-daemon.sh start datanode")

                if dNchoice == 4:
                    os.system("sleep 5")
                    os.system("jps")

HadoopStart()
