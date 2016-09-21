从thc-hydra源码里乱七八槽抠一顿下来：
gcc -fPIE -shared -o hydra-rdp.so  hydra-rdp.c hydra-mod.c ntlm.c sasl.c bfg.c hydra-time.c -DLIBOPENSSL -DHAVE_ZLIB -DHAVE_MATH_H -fPIC -lssl
