从thc-hydra源码里乱七八槽抠一顿下来：
gcc -fPIE -shared -o hydra-rdp.so  hydra-rdp.c hydra-mod.c ntlm.c sasl.c bfg.c hydra-time.c -DLIBOPENSSL -DHAVE_ZLIB -DHAVE_MATH_H -fPIC -lssl

源码实现RDP登录过程使用了全局变量，导致无法多线程调用。
