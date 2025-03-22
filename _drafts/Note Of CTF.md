
- FSLS
	- file 查看基本信息，是否 stripped
	- strings 查看字符串信息
	- ltrace 跟踪调用的库
	- strace 类似 ltrace

- Docker
	- sudo service docker restart


- libc
	- ldd --version
	- ldd "可执行文件"
	- strings "lbc" | grep "GNU"
- libc all in one
	- cat ./list
	- ldd -v "可执行文件"
	- 
patchelf --set-interpreter "ld" "pwn"
ldd “pwn”
patchelf --replace-needed "=> 前 libc 名" "libc" "pwn"

/etc/sudo tar -cf /dev/bull /dev/null --checkpoint=1 20 --checkpoint-action=exec=ps -ef