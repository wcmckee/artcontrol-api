# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# dhcpd.leases

# <codecell>

ls

# <codecell>

dh = open('dhcpd.leases', 'r')

# <codecell>

with open ('dhcpd.leases', "r") as myfile:
    data=myfile.readlines()

# <codecell>

print data

# <codecell>

from pyparsing import Word, alphas
greet = Word( alphas ) + "," + Word( alphas ) + "!" # <-- grammar defined here
hello = "Hello, World!"
print (hello, "->", greet.parseString( hello ))

# <codecell>


# <codecell>

print newf

# <codecell>

for f in dh:
    print f.read()

# <codecell>

lisbleh = []

# <codecell>

sample = r"""\
lease 10.3.1.128 {
  starts 2 2014/01/28 04:04:06;
  ends 3 2014/01/29 04:04:06;
  tstp 3 2014/01/29 04:04:06;
  cltt 2 2014/01/28 04:04:06;
  binding state free;
  hardware ethernet 70:f9:27:a5:7d:9c;
  uid "\001p\371'\245}\234";
}
lease 10.3.1.166 {
  starts 2 2014/01/28 08:35:02;
  ends 3 2014/01/29 08:35:02;
  tstp 3 2014/01/29 08:35:02;
  cltt 2 2014/01/28 08:35:02;
  binding state free;
  hardware ethernet 78:e8:b6:a6:27:69;
}
lease 10.3.1.161 {
  starts 3 2014/01/29 13:41:33;
  ends 3 2014/01/29 23:56:55;
  tstp 3 2014/01/29 23:56:55;
  cltt 3 2014/01/29 13:41:33;
  binding state free;
  hardware ethernet 00:0e:08:ec:75:b9;
  uid "\001\000\016\010\354u\271";
}
lease 10.3.1.139 {
  starts 3 2014/01/29 01:35:36;
  ends 4 2014/01/30 01:35:36;
  tstp 4 2014/01/30 01:35:36;
  cltt 3 2014/01/29 01:35:36;
  binding state free;
  hardware ethernet 28:cc:01:bb:6c:d2;
  uid "\001(\314\001\273l\322";
}
lease 10.3.1.174 {
  starts 3 2014/01/29 05:27:12;
  ends 4 2014/01/30 05:27:12;
  tstp 4 2014/01/30 05:27:12;
  cltt 3 2014/01/29 05:27:12;
  binding state free;
  hardware ethernet 20:59:a0:a0:52:0f;
}
lease 10.3.1.172 {
  starts 4 2014/01/30 22:22:18;
  ends 5 2014/01/31 01:47:49;
  tstp 5 2014/01/31 01:47:49;
  cltt 4 2014/01/30 22:22:18;
  binding state free;
  hardware ethernet 00:13:d3:ce:e5:a0;
}
lease 10.3.1.178 {
  starts 4 2014/01/30 03:19:13;
  ends 5 2014/01/31 03:19:13;
  tstp 5 2014/01/31 03:19:13;
  cltt 4 2014/01/30 03:19:13;
  binding state free;
  hardware ethernet 00:03:7e:ec:61:d1;
}
lease 10.3.1.125 {
  starts 4 2014/01/30 08:15:50;
  ends 5 2014/01/31 08:15:50;
  tstp 5 2014/01/31 08:15:50;
  cltt 4 2014/01/30 08:15:50;
  binding state free;
  hardware ethernet f0:72:8c:01:75:b9;
  uid "\001\360r\214\001u\271";
}
lease 10.3.1.171 {
  starts 4 2014/01/30 23:00:47;
  ends 5 2014/01/31 23:00:47;
  tstp 5 2014/01/31 23:00:47;
  cltt 4 2014/01/30 23:00:47;
  binding state free;
  hardware ethernet 00:13:d3:ce:e5:a0;
}
lease 10.3.1.181 {
  starts 5 2014/01/31 00:44:23;
  ends 6 2014/02/01 00:44:23;
  tstp 6 2014/02/01 00:44:23;
  cltt 5 2014/01/31 00:44:23;
  binding state free;
  hardware ethernet 50:9f:27:de:14:f7;
}
lease 10.3.1.129 {
  starts 5 2014/01/24 22:18:35;
  ends 6 2014/02/01 18:18:35;
  tstp 6 2014/02/01 18:18:35;
  cltt 5 2014/01/24 22:18:35;
  binding state free;
  hardware ethernet 70:56:81:81:7d:e3;
  uid "\001pV\201\201}\343";
}
lease 10.3.1.176 {
  starts 6 2014/02/01 06:43:45;
  ends 0 2014/02/02 06:43:45;
  tstp 0 2014/02/02 06:43:45;
  cltt 6 2014/02/01 06:43:45;
  binding state free;
  hardware ethernet b4:07:f9:8a:bb:c4;
  uid "\001\264\007\371\212\273\304";
}
lease 10.3.1.188 {
  starts 6 2014/02/01 07:16:14;
  ends 0 2014/02/02 07:16:14;
  tstp 0 2014/02/02 07:16:14;
  cltt 6 2014/02/01 07:16:14;
  binding state free;
  hardware ethernet b4:07:f9:99:fd:ef;
  uid "\001\264\007\371\231\375\357";
}
lease 10.3.1.157 {
  starts 0 2014/02/02 00:15:35;
  ends 1 2014/02/03 00:15:35;
  tstp 1 2014/02/03 00:15:35;
  cltt 0 2014/02/02 00:15:35;
  binding state free;
  hardware ethernet 00:c6:b1:40:8f:b2;
}
lease 10.3.1.191 {
  starts 0 2014/02/02 05:34:27;
  ends 1 2014/02/03 05:34:27;
  tstp 1 2014/02/03 05:34:27;
  cltt 0 2014/02/02 05:34:27;
  binding state free;
  hardware ethernet 74:e1:b6:02:8d:66;
  uid "\001t\341\266\002\215f";
}
lease 10.3.1.193 {
  starts 0 2014/02/02 07:27:09;
  ends 1 2014/02/03 07:27:09;
  tstp 1 2014/02/03 07:27:09;
  cltt 0 2014/02/02 07:27:09;
  binding state free;
  hardware ethernet 8c:c5:e1:05:0f:85;
}
lease 10.3.1.204 {
  starts 2 2014/02/04 06:39:04;
  ends 3 2014/02/05 06:39:04;
  tstp 3 2014/02/05 06:39:04;
  cltt 2 2014/02/04 06:39:04;
  binding state free;
  hardware ethernet 4c:0b:3a:b0:51:e4;
}
lease 10.3.1.205 {
  starts 2 2014/02/04 08:12:40;
  ends 3 2014/02/05 08:12:40;
  tstp 3 2014/02/05 08:12:40;
  cltt 2 2014/02/04 08:12:40;
  binding state free;
  hardware ethernet 00:13:02:ca:1b:de;
}
lease 10.3.1.207 {
  starts 3 2014/02/05 08:24:13;
  ends 4 2014/02/06 08:24:13;
  tstp 4 2014/02/06 08:24:13;
  cltt 3 2014/02/05 08:24:13;
  binding state free;
  hardware ethernet d8:b3:77:74:e6:9f;
  uid "\001\330\263wt\346\237";
}
lease 10.3.1.121 {
  starts 3 2014/02/05 22:42:00;
  ends 4 2014/02/06 22:42:00;
  tstp 4 2014/02/06 22:42:00;
  cltt 3 2014/02/05 22:42:00;
  binding state free;
  hardware ethernet 38:48:4c:6d:5e:76;
  uid "\0018HLm^v";
}
lease 10.3.1.210 {
  starts 4 2014/02/06 06:42:08;
  ends 5 2014/02/07 06:42:08;
  tstp 5 2014/02/07 06:42:08;
  cltt 4 2014/02/06 06:42:08;
  binding state free;
  hardware ethernet 00:e3:b2:bf:fa:5a;
  uid "\001\000\343\262\277\372Z";
}
lease 10.3.1.198 {
  starts 4 2014/02/06 19:25:32;
  ends 5 2014/02/07 19:25:32;
  tstp 5 2014/02/07 19:25:32;
  cltt 4 2014/02/06 19:25:32;
  binding state free;
  hardware ethernet 88:f4:88:6e:ac:9a;
}
lease 10.3.1.212 {
  starts 5 2014/02/07 01:51:38;
  ends 6 2014/02/08 01:51:38;
  tstp 6 2014/02/08 01:51:38;
  cltt 5 2014/02/07 01:51:38;
  binding state free;
  hardware ethernet 20:68:9d:24:1b:a1;
  uid "\001 h\235$\033\241";
}
lease 10.3.1.214 {
  starts 5 2014/02/07 02:30:30;
  ends 6 2014/02/08 02:30:30;
  tstp 6 2014/02/08 02:30:30;
  cltt 5 2014/02/07 02:30:30;
  binding state free;
  hardware ethernet 4c:72:b9:85:25:52;
}
lease 10.3.1.213 {
  starts 5 2014/02/07 02:30:32;
  ends 6 2014/02/08 02:30:32;
  tstp 6 2014/02/08 02:30:32;
  cltt 5 2014/02/07 02:30:32;
  binding state free;
  hardware ethernet 20:68:9d:24:1b:a1;
}
lease 10.3.1.186 {
  starts 5 2014/02/07 04:18:01;
  ends 6 2014/02/08 04:18:01;
  tstp 6 2014/02/08 04:18:01;
  cltt 5 2014/02/07 04:18:01;
  binding state free;
  hardware ethernet 80:96:b1:51:51:75;
}
lease 10.3.1.215 {
  starts 5 2014/02/07 05:04:10;
  ends 6 2014/02/08 05:04:10;
  tstp 6 2014/02/08 05:04:10;
  cltt 5 2014/02/07 05:04:10;
  binding state free;
  hardware ethernet 00:03:7e:e7:d1:f0;
}
lease 10.3.1.152 {
  starts 5 2014/02/07 21:55:36;
  ends 6 2014/02/08 21:55:36;
  tstp 6 2014/02/08 21:55:36;
  cltt 5 2014/02/07 21:55:36;
  binding state free;
  hardware ethernet 00:c4:91:00:11:6c;
}
lease 10.3.1.208 {
  starts 6 2014/02/08 02:18:04;
  ends 0 2014/02/09 02:18:04;
  tstp 0 2014/02/09 02:18:04;
  cltt 6 2014/02/08 02:18:04;
  binding state free;
  hardware ethernet 88:f4:88:6e:9b:a9;
}
lease 10.3.1.190 {
  starts 0 2014/02/09 00:25:32;
  ends 1 2014/02/10 00:25:32;
  tstp 1 2014/02/10 00:25:32;
  cltt 0 2014/02/09 00:25:32;
  binding state free;
  hardware ethernet f0:cb:a1:d2:a7:a0;
  uid "\001\360\313\241\322\247\240";
}
lease 10.3.1.217 {
  starts 0 2014/02/09 03:59:45;
  ends 1 2014/02/10 03:59:45;
  tstp 1 2014/02/10 03:59:45;
  cltt 0 2014/02/09 03:59:45;
  binding state free;
  hardware ethernet 90:5f:2e:61:78:f2;
}
lease 10.3.1.131 {
  starts 0 2014/02/09 23:48:40;
  ends 1 2014/02/10 23:48:40;
  tstp 1 2014/02/10 23:48:40;
  cltt 0 2014/02/09 23:48:40;
  binding state free;
  hardware ethernet 60:d8:19:26:a6:98;
  uid "\001`\330\031&\246\230";
}
lease 10.3.1.173 {
  starts 1 2014/02/10 01:47:02;
  ends 2 2014/02/11 01:47:02;
  tstp 2 2014/02/11 01:47:02;
  cltt 1 2014/02/10 01:47:02;
  binding state free;
  hardware ethernet 4c:0b:3a:7d:51:1b;
}
lease 10.3.1.228 {
  starts 2 2014/02/11 02:06:07;
  ends 2 2014/02/11 02:12:21;
  tstp 2 2014/02/11 02:12:21;
  cltt 2 2014/02/11 02:06:07;
  binding state free;
  hardware ethernet 00:1e:68:75:88:e3;
}
lease 10.3.1.144 {
  starts 1 2014/02/10 02:30:28;
  ends 2 2014/02/11 02:30:28;
  tstp 2 2014/02/11 02:30:28;
  cltt 1 2014/02/10 02:30:28;
  binding state free;
  hardware ethernet b8:5e:7b:79:2e:de;
  uid "\001\270^{y.\336";
}
lease 10.3.1.226 {
  starts 1 2014/02/10 06:12:00;
  ends 2 2014/02/11 06:12:00;
  tstp 2 2014/02/11 06:12:00;
  cltt 1 2014/02/10 06:12:00;
  binding state free;
  hardware ethernet f4:55:9c:6c:5d:85;
}
lease 10.3.1.201 {
  starts 2 2014/02/04 02:47:27;
  ends 2 2014/02/11 22:47:27;
  tstp 2 2014/02/11 22:47:27;
  cltt 2 2014/02/04 02:47:27;
  binding state free;
  hardware ethernet b4:f0:ab:02:c3:08;
  uid "\001\264\360\253\002\303\010";
}
lease 10.3.1.227 {
  starts 2 2014/02/11 01:43:04;
  ends 3 2014/02/12 01:43:04;
  tstp 3 2014/02/12 01:43:04;
  cltt 2 2014/02/11 01:43:04;
  binding state free;
  hardware ethernet 00:1e:68:75:88:e3;
  uid "\001\000\036hu\210\343";
}
lease 10.3.1.229 {
  starts 2 2014/02/11 03:14:27;
  ends 3 2014/02/12 03:14:27;
  tstp 3 2014/02/12 03:14:27;
  cltt 2 2014/02/11 03:14:27;
  binding state free;
  hardware ethernet 00:c0:9f:7d:e9:21;
  uid "\001\000\300\237}\351!";
}
lease 10.3.1.230 {
  starts 2 2014/02/11 03:39:49;
  ends 3 2014/02/12 03:39:49;
  tstp 3 2014/02/12 03:39:49;
  cltt 2 2014/02/11 03:39:49;
  binding state free;
  hardware ethernet 00:c0:9f:7d:e9:21;
}
lease 10.3.1.234 {
  starts 2 2014/02/11 19:43:31;
  ends 3 2014/02/12 19:43:31;
  tstp 3 2014/02/12 19:43:31;
  cltt 2 2014/02/11 19:43:31;
  binding state free;
  hardware ethernet 8c:7b:9d:d3:bf:89;
  uid "\001\214{\235\323\277\211";
}
lease 10.3.1.235 {
  starts 2 2014/02/11 22:07:00;
  ends 3 2014/02/12 22:07:00;
  tstp 3 2014/02/12 22:07:00;
  cltt 2 2014/02/11 22:07:00;
  binding state free;
  hardware ethernet 08:11:96:31:ce:a4;
  uid "\001\010\021\2261\316\244";
}
lease 10.3.1.237 {
  starts 3 2014/02/12 02:10:17;
  ends 4 2014/02/13 02:10:17;
  tstp 4 2014/02/13 02:10:17;
  cltt 3 2014/02/12 02:10:17;
  binding state free;
  hardware ethernet 20:6a:8a:71:27:09;
}
lease 10.3.1.236 {
  starts 3 2014/02/12 02:33:01;
  ends 4 2014/02/13 02:33:01;
  tstp 4 2014/02/13 02:33:01;
  cltt 3 2014/02/12 02:33:01;
  binding state free;
  hardware ethernet 20:6a:8a:71:27:09;
  uid "\001 j\212q'\011";
}
lease 10.3.1.219 {
  starts 3 2014/02/12 04:38:01;
  ends 4 2014/02/13 04:38:01;
  tstp 4 2014/02/13 04:38:01;
  cltt 3 2014/02/12 04:38:01;
  binding state free;
  hardware ethernet 00:07:88:8f:27:08;
}
lease 10.3.1.248 {
  starts 4 2014/02/13 01:19:44;
  ends 5 2014/02/14 01:19:44;
  tstp 5 2014/02/14 01:19:44;
  cltt 4 2014/02/13 01:19:44;
  binding state free;
  hardware ethernet 0c:14:20:8f:c7:b5;
  uid "\001\014\024 \217\307\265";
}
lease 10.3.1.211 {
  starts 4 2014/02/06 06:59:24;
  ends 5 2014/02/14 02:59:24;
  tstp 5 2014/02/14 02:59:24;
  cltt 4 2014/02/06 06:59:24;
  binding state free;
  hardware ethernet dc:2b:61:1e:96:99;
  uid "\001\334+a\036\226\231";
}
lease 10.3.1.249 {
  starts 4 2014/02/13 04:43:02;
  ends 5 2014/02/14 04:43:02;
  tstp 5 2014/02/14 04:43:02;
  cltt 4 2014/02/13 04:43:02;
  binding state free;
  hardware ethernet 24:ec:99:1c:3b:98;
}
lease 10.3.1.149 {
  starts 4 2014/02/13 07:27:59;
  ends 5 2014/02/14 07:27:59;
  tstp 5 2014/02/14 07:27:59;
  cltt 4 2014/02/13 07:27:59;
  binding state free;
  hardware ethernet 3c:df:bd:2f:45:4e;
}
lease 10.3.1.225 {
  starts 4 2014/02/13 19:03:00;
  ends 5 2014/02/14 19:03:00;
  tstp 5 2014/02/14 19:03:00;
  cltt 4 2014/02/13 19:03:00;
  binding state free;
  hardware ethernet 00:0c:b2:13:b3:35;
}
lease 10.3.1.245 {
  starts 4 2014/02/13 19:30:18;
  ends 5 2014/02/14 19:30:18;
  tstp 5 2014/02/14 19:30:18;
  cltt 4 2014/02/13 19:30:18;
  binding state free;
  hardware ethernet e4:2d:02:33:ed:7d;
}
lease 10.3.1.232 {
  starts 5 2014/02/14 04:10:08;
  ends 6 2014/02/15 04:10:08;
  tstp 6 2014/02/15 04:10:08;
  cltt 5 2014/02/14 04:10:08;
  binding state free;
  hardware ethernet 48:a2:2d:f1:59:36;
}
lease 10.3.1.251 {
  starts 5 2014/02/14 06:13:59;
  ends 6 2014/02/15 06:13:59;
  tstp 6 2014/02/15 06:13:59;
  cltt 5 2014/02/14 06:13:59;
  binding state free;
  hardware ethernet e0:b2:f1:e1:17:7e;
}
lease 10.3.1.127 {
  starts 5 2014/02/14 21:45:02;
  ends 6 2014/02/15 21:45:02;
  tstp 6 2014/02/15 21:45:02;
  cltt 5 2014/02/14 21:45:02;
  binding state free;
  hardware ethernet 00:11:7f:1a:43:08;
}
lease 10.3.1.114 {
  starts 5 2014/02/14 21:51:33;
  ends 6 2014/02/15 21:51:33;
  tstp 6 2014/02/15 21:51:33;
  cltt 5 2014/02/14 21:51:33;
  binding state free;
  hardware ethernet ec:55:f9:16:f3:8c;
  uid "\001\354U\371\026\363\214";
}
lease 10.3.1.25 {
  starts 5 2014/02/14 22:05:20;
  ends 6 2014/02/15 22:05:20;
  tstp 6 2014/02/15 22:05:20;
  cltt 5 2014/02/14 22:05:20;
  binding state free;
  hardware ethernet 08:7a:4c:cd:d7:d8;
}
lease 10.3.1.100 {
  starts 5 2014/02/14 23:39:33;
  ends 6 2014/02/15 23:39:33;
  tstp 6 2014/02/15 23:39:33;
  cltt 5 2014/02/14 23:39:33;
  binding state free;
  hardware ethernet 98:52:b1:13:23:a9;
  uid "\001\230R\261\023#\251";
}
lease 10.3.1.27 {
  starts 6 2014/02/15 00:07:48;
  ends 0 2014/02/16 00:07:48;
  tstp 0 2014/02/16 00:07:48;
  cltt 6 2014/02/15 00:07:48;
  binding state free;
  hardware ethernet 00:e0:5c:07:12:65;
}
lease 10.3.1.134 {
  starts 6 2014/02/15 00:42:43;
  ends 0 2014/02/16 00:42:43;
  tstp 0 2014/02/16 00:42:43;
  cltt 6 2014/02/15 00:42:43;
  binding state free;
  hardware ethernet d0:e7:82:47:b8:f3;
}
lease 10.3.1.23 {
  starts 6 2014/02/15 01:36:30;
  ends 0 2014/02/16 01:36:30;
  tstp 0 2014/02/16 01:36:30;
  cltt 6 2014/02/15 01:36:30;
  binding state free;
  hardware ethernet 00:1e:4c:a2:68:3a;
}
lease 10.3.1.28 {
  starts 6 2014/02/15 03:39:12;
  ends 0 2014/02/16 03:39:12;
  tstp 0 2014/02/16 03:39:12;
  cltt 6 2014/02/15 03:39:12;
  binding state free;
  hardware ethernet 40:4d:8e:bf:1c:26;
}
lease 10.3.1.29 {
  starts 6 2014/02/15 04:20:09;
  ends 0 2014/02/16 04:20:09;
  tstp 0 2014/02/16 04:20:09;
  cltt 6 2014/02/15 04:20:09;
  binding state free;
  hardware ethernet e0:b2:f1:81:13:c1;
}
lease 10.3.1.107 {
  starts 6 2014/02/15 04:49:35;
  ends 0 2014/02/16 04:49:35;
  tstp 0 2014/02/16 04:49:35;
  cltt 6 2014/02/15 04:49:35;
  binding state free;
  hardware ethernet 4c:0b:3a:74:17:7c;
}
lease 10.3.1.30 {
  starts 6 2014/02/15 05:00:21;
  ends 0 2014/02/16 05:00:21;
  tstp 0 2014/02/16 05:00:21;
  cltt 6 2014/02/15 05:00:21;
  binding state free;
  hardware ethernet 18:1e:b0:69:fe:cf;
  uid "\001\030\036\260i\376\317";
}
lease 10.3.1.31 {
  starts 6 2014/02/15 05:23:28;
  ends 0 2014/02/16 05:22:28;
  tstp 0 2014/02/16 05:22:28;
  cltt 6 2014/02/15 05:23:28;
  binding state free;
  hardware ethernet 4c:0b:3a:7c:20:14;
}
lease 10.3.1.33 {
  starts 6 2014/02/15 05:39:18;
  ends 0 2014/02/16 05:39:18;
  tstp 0 2014/02/16 05:39:18;
  cltt 6 2014/02/15 05:39:18;
  binding state free;
  hardware ethernet c4:88:e5:a7:ca:58;
  uid "\001\304\210\345\247\312X";
}
lease 10.3.1.26 {
  starts 0 2014/02/16 00:15:40;
  ends 1 2014/02/17 00:15:40;
  tstp 1 2014/02/17 00:15:40;
  cltt 0 2014/02/16 00:15:40;
  binding state free;
  hardware ethernet 88:a7:3c:88:8c:26;
}
lease 10.3.1.183 {
  starts 2 2014/02/11 04:35:18;
  ends 3 2014/02/19 00:35:18;
  tstp 3 2014/02/19 00:35:18;
  cltt 2 2014/02/11 04:35:18;
  binding state free;
  hardware ethernet 8c:7b:9d:74:1b:cb;
  uid "\001\214{\235t\033\313";
}
lease 10.3.1.231 {
  starts 2 2014/02/11 05:00:26;
  ends 3 2014/02/19 01:00:26;
  tstp 3 2014/02/19 01:00:26;
  cltt 2 2014/02/11 05:00:26;
  binding state free;
  hardware ethernet 5c:f9:38:15:74:3f;
  uid "\001\\\3718\025t?";
}
lease 10.3.1.34 {
  starts 2 2014/02/18 03:25:52;
  ends 3 2014/02/19 03:25:52;
  tstp 3 2014/02/19 03:25:52;
  cltt 2 2014/02/18 03:25:52;
  binding state free;
  hardware ethernet 00:1c:23:4e:33:2b;
}
lease 10.3.1.209 {
  starts 2 2014/02/18 07:09:21;
  ends 3 2014/02/19 07:09:21;
  tstp 3 2014/02/19 07:09:21;
  cltt 2 2014/02/18 07:09:21;
  binding state free;
  hardware ethernet 00:6b:0e:01:fe:b6;
}
lease 10.3.1.38 {
  starts 3 2014/02/19 00:33:52;
  ends 4 2014/02/20 00:33:52;
  tstp 4 2014/02/20 00:33:52;
  cltt 3 2014/02/19 00:33:52;
  binding state free;
  hardware ethernet 14:89:fd:7a:f6:3c;
  uid "\001\024\211\375z\366<";
}
lease 10.3.1.241 {
  starts 3 2014/02/12 04:58:52;
  ends 4 2014/02/20 00:58:52;
  tstp 4 2014/02/20 00:58:52;
  cltt 3 2014/02/12 04:58:52;
  binding state free;
  hardware ethernet 54:ea:a8:c4:fd:1b;
  uid "\001T\352\250\304\375\033";
}
lease 10.3.1.46 {
  starts 3 2014/02/19 04:47:39;
  ends 4 2014/02/20 04:47:39;
  tstp 4 2014/02/20 04:47:39;
  cltt 3 2014/02/19 04:47:39;
  binding state free;
  hardware ethernet 8c:00:6d:4a:98:f7;
  uid "\001\214\000mJ\230\367";
}
lease 10.3.1.47 {
  starts 3 2014/02/19 04:48:16;
  ends 4 2014/02/20 04:48:16;
  tstp 4 2014/02/20 04:48:16;
  cltt 3 2014/02/19 04:48:16;
  binding state free;
  hardware ethernet cc:3a:61:a9:10:f7;
  uid "\001\314:a\251\020\367";
}
lease 10.3.1.24 {
  starts 3 2014/02/19 06:27:10;
  ends 4 2014/02/20 06:27:10;
  tstp 4 2014/02/20 06:27:10;
  cltt 3 2014/02/19 06:27:10;
  binding state free;
  hardware ethernet 00:13:02:ca:1b:de;
}
lease 10.3.1.50 {
  starts 4 2014/02/20 04:32:05;
  ends 5 2014/02/21 04:32:05;
  tstp 5 2014/02/21 04:32:05;
  cltt 4 2014/02/20 04:32:05;
  binding state free;
  hardware ethernet 00:27:15:82:68:10;
}
lease 10.3.1.138 {
  starts 4 2014/02/20 19:34:11;
  ends 5 2014/02/21 19:34:11;
  tstp 5 2014/02/21 19:34:11;
  cltt 4 2014/02/20 19:34:11;
  binding state free;
  hardware ethernet d0:2d:b3:96:a6:01;
}
lease 10.3.1.203 {
  starts 5 2014/02/14 00:15:54;
  ends 5 2014/02/21 20:15:54;
  tstp 5 2014/02/21 20:15:54;
  cltt 5 2014/02/14 00:15:54;
  binding state free;
  hardware ethernet b8:78:2e:b1:7d:de;
  uid "\001\270x.\261}\336";
}
lease 10.3.1.52 {
  starts 4 2014/02/20 22:27:45;
  ends 5 2014/02/21 22:27:45;
  tstp 5 2014/02/21 22:27:45;
  cltt 4 2014/02/20 22:27:45;
  binding state free;
  hardware ethernet 18:00:2d:3f:d1:3d;
}
lease 10.3.1.53 {
  starts 4 2014/02/20 23:43:18;
  ends 5 2014/02/21 23:43:18;
  tstp 5 2014/02/21 23:43:18;
  cltt 4 2014/02/20 23:43:18;
  binding state free;
  hardware ethernet 00:25:22:98:f2:13;
}
lease 10.3.1.137 {
  starts 5 2014/02/21 00:21:29;
  ends 6 2014/02/22 00:21:29;
  tstp 6 2014/02/22 00:21:29;
  cltt 5 2014/02/21 00:21:29;
  binding state free;
  hardware ethernet d0:2d:b3:e4:a6:8d;
}
lease 10.3.1.54 {
  starts 5 2014/02/21 03:54:10;
  ends 6 2014/02/22 03:54:10;
  tstp 6 2014/02/22 03:54:10;
  cltt 5 2014/02/21 03:54:10;
  binding state free;
  hardware ethernet 00:1f:3a:bb:97:22;
  uid "\001\000\037:\273\227\"";
}
lease 10.3.1.244 {
  starts 5 2014/02/21 13:27:50;
  ends 6 2014/02/22 13:27:50;
  tstp 6 2014/02/22 13:27:50;
  cltt 5 2014/02/21 13:27:50;
  binding state free;
  hardware ethernet 4c:0b:3a:74:19:00;
}
lease 10.3.1.49 {
  starts 6 2014/02/22 00:14:06;
  ends 0 2014/02/23 00:14:06;
  tstp 0 2014/02/23 00:14:06;
  cltt 6 2014/02/22 00:14:06;
  binding state free;
  hardware ethernet 5c:0a:5b:3b:aa:75;
  uid "\001\\\012[;\252u";
}
lease 10.3.1.185 {
  starts 6 2014/02/22 23:58:40;
  ends 0 2014/02/23 00:58:40;
  tstp 0 2014/02/23 00:58:40;
  cltt 6 2014/02/22 23:58:40;
  binding state free;
  hardware ethernet c8:b5:b7:74:da:37;
  uid "\001\310\265\267t\3327";
}
lease 10.3.1.177 {
  starts 0 2014/02/23 01:07:07;
  ends 0 2014/02/23 01:37:07;
  tstp 0 2014/02/23 01:37:07;
  cltt 0 2014/02/23 01:07:07;
  binding state free;
  hardware ethernet 0c:37:dc:f6:c0:4d;
}
lease 10.3.1.58 {
  starts 6 2014/02/22 02:03:28;
  ends 0 2014/02/23 02:03:28;
  tstp 0 2014/02/23 02:03:28;
  cltt 6 2014/02/22 02:03:28;
  binding state free;
  hardware ethernet 90:00:4e:53:bd:bf;
  uid "\001\220\000NS\275\277";
}
lease 10.3.1.60 {
  starts 6 2014/02/22 03:42:45;
  ends 0 2014/02/23 03:42:45;
  tstp 0 2014/02/23 03:42:45;
  cltt 6 2014/02/22 03:42:45;
  binding state free;
  hardware ethernet 78:52:1a:46:2c:32;
  uid "\001xR\032F,2";
}
lease 10.3.1.103 {
  starts 0 2014/02/23 03:27:44;
  ends 0 2014/02/23 03:57:44;
  tstp 0 2014/02/23 03:57:44;
  cltt 0 2014/02/23 03:27:44;
  binding state free;
  hardware ethernet 0c:37:dc:f7:52:bb;
}
lease 10.3.1.59 {
  starts 6 2014/02/22 04:13:01;
  ends 0 2014/02/23 04:13:01;
  tstp 0 2014/02/23 04:13:01;
  cltt 6 2014/02/22 04:13:01;
  binding state free;
  hardware ethernet bc:20:a4:2d:0e:94;
  uid "\001\274 \244-\016\224";
}
lease 10.3.1.126 {
  starts 6 2014/02/22 08:08:49;
  ends 0 2014/02/23 08:08:49;
  tstp 0 2014/02/23 08:08:49;
  cltt 6 2014/02/22 08:08:49;
  binding state free;
  hardware ethernet 00:1b:77:51:27:2b;
  uid "\001\000\033wQ'+";
}
lease 10.3.1.168 {
  starts 0 2014/02/16 00:26:19;
  ends 0 2014/02/23 20:26:19;
  tstp 0 2014/02/23 20:26:19;
  cltt 0 2014/02/16 00:26:19;
  binding state free;
  hardware ethernet d8:d1:cb:07:48:74;
  uid "\001\330\321\313\007Ht";
}
lease 10.3.1.62 {
  starts 0 2014/02/23 20:42:07;
  ends 0 2014/02/23 21:12:07;
  tstp 0 2014/02/23 21:12:07;
  cltt 0 2014/02/23 20:42:07;
  binding state free;
  hardware ethernet dc:ce:bc:84:c3:45;
}
lease 10.3.1.63 {
  starts 0 2014/02/23 21:02:33;
  ends 0 2014/02/23 21:32:33;
  tstp 0 2014/02/23 21:32:33;
  cltt 0 2014/02/23 21:02:33;
  binding state free;
  hardware ethernet 90:5f:2e:ff:22:a2;
  uid "\001\220_.\377\"\242";
}
lease 10.3.1.120 {
  starts 1 2014/02/24 00:18:50;
  ends 1 2014/02/24 00:48:50;
  tstp 1 2014/02/24 00:48:50;
  cltt 1 2014/02/24 00:18:50;
  binding state free;
  hardware ethernet 14:89:fd:7b:65:3a;
  uid "\001\024\211\375{e:";
}
lease 10.3.1.57 {
  starts 1 2014/02/24 03:53:14;
  ends 1 2014/02/24 04:23:14;
  tstp 1 2014/02/24 04:23:14;
  cltt 1 2014/02/24 03:53:14;
  binding state free;
  hardware ethernet 30:87:30:fa:fb:6b;
  uid "\0010\2070\372\373k";
}
lease 10.3.1.56 {
  starts 1 2014/02/24 04:34:07;
  ends 1 2014/02/24 05:34:07;
  tstp 1 2014/02/24 05:34:07;
  cltt 1 2014/02/24 04:34:07;
  binding state free;
  hardware ethernet 5c:f9:38:3e:c8:20;
  uid "\001\\\3718>\310 ";
}
lease 10.3.1.175 {
  starts 1 2014/02/24 05:30:08;
  ends 1 2014/02/24 06:00:08;
  tstp 1 2014/02/24 06:00:08;
  cltt 1 2014/02/24 05:30:08;
  binding state free;
  hardware ethernet 98:e7:9a:10:0d:8d;
}
lease 10.3.1.65 {
  starts 2 2014/02/25 02:16:52;
  ends 2 2014/02/25 02:46:52;
  tstp 2 2014/02/25 02:46:52;
  cltt 2 2014/02/25 02:16:52;
  binding state free;
  hardware ethernet 0c:bd:51:74:cd:3c;
}
lease 10.3.1.68 {
  starts 2 2014/02/25 02:18:10;
  ends 2 2014/02/25 02:48:10;
  tstp 2 2014/02/25 02:48:10;
  cltt 2 2014/02/25 02:18:10;
  binding state free;
  hardware ethernet 6c:83:36:06:7a:f9;
  uid "\001l\2036\006z\371";
}
lease 10.3.1.66 {
  starts 2 2014/02/25 03:13:12;
  ends 2 2014/02/25 03:43:12;
  tstp 2 2014/02/25 03:43:12;
  cltt 2 2014/02/25 03:13:12;
  binding state free;
  hardware ethernet d8:31:cf:ad:1a:97;
  uid "\001\3301\317\255\032\227";
}
lease 10.3.1.36 {
  starts 2 2014/02/25 03:52:56;
  ends 2 2014/02/25 04:22:56;
  tstp 2 2014/02/25 04:22:56;
  cltt 2 2014/02/25 03:52:56;
  binding state free;
  hardware ethernet d0:2d:b3:95:a5:82;
}
lease 10.3.1.170 {
  starts 2 2014/02/25 03:58:43;
  ends 2 2014/02/25 04:28:43;
  tstp 2 2014/02/25 04:28:43;
  cltt 2 2014/02/25 03:58:43;
  binding state free;
  hardware ethernet b8:c6:8e:80:be:c4;
  uid "\001\270\306\216\200\276\304";
}
lease 10.3.1.250 {
  starts 2 2014/02/25 05:05:13;
  ends 2 2014/02/25 06:05:13;
  tstp 2 2014/02/25 06:05:13;
  cltt 2 2014/02/25 05:05:13;
  binding state free;
  hardware ethernet 90:b2:1f:2c:16:6b;
  uid "\001\220\262\037,\026k";
}
lease 10.3.1.102 {
  starts 2 2014/02/25 06:30:03;
  ends 2 2014/02/25 07:00:03;
  tstp 2 2014/02/25 07:00:03;
  cltt 2 2014/02/25 06:30:03;
  binding state free;
  hardware ethernet 90:5f:2e:f6:7a:83;
}
lease 10.3.1.233 {
  starts 2 2014/02/25 07:25:06;
  ends 2 2014/02/25 07:55:06;
  tstp 2 2014/02/25 07:55:06;
  cltt 2 2014/02/25 07:25:06;
  binding state free;
  hardware ethernet bc:85:1f:01:ba:4d;
  uid "\001\274\205\037\001\272M";
}
lease 10.3.1.192 {
  starts 2 2014/02/18 06:30:13;
  ends 3 2014/02/26 02:30:13;
  tstp 3 2014/02/26 02:30:13;
  cltt 2 2014/02/18 06:30:13;
  binding state free;
  hardware ethernet 70:73:cb:49:66:bc;
  uid "\001ps\313If\274";
}
lease 10.3.1.37 {
  starts 3 2014/02/26 03:53:09;
  ends 3 2014/02/26 04:23:09;
  tstp 3 2014/02/26 04:23:09;
  cltt 3 2014/02/26 03:53:09;
  binding state free;
  hardware ethernet 78:e8:b6:a6:01:f3;
}
lease 10.3.1.194 {
  starts 3 2014/02/26 05:50:51;
  ends 3 2014/02/26 06:20:51;
  tstp 3 2014/02/26 06:20:51;
  cltt 3 2014/02/26 05:50:51;
  binding state free;
  hardware ethernet 50:a4:c8:0e:0c:78;
  uid "\001P\244\310\016\014x";
}
lease 10.3.1.182 {
  starts 3 2014/02/26 07:18:07;
  ends 3 2014/02/26 07:48:07;
  tstp 3 2014/02/26 07:48:07;
  cltt 3 2014/02/26 07:18:07;
  binding state free;
  hardware ethernet b0:35:8d:e6:c3:c0;
  uid "\001\2605\215\346\303\300";
}
lease 10.3.1.75 {
  starts 3 2014/02/26 08:18:23;
  ends 3 2014/02/26 08:20:23;
  tstp 3 2014/02/26 08:20:23;
  cltt 3 2014/02/26 08:18:23;
  binding state free;
  hardware ethernet d8:90:e8:63:3a:ae;
  uid "\001\330\220\350c:\256";
  client-hostname "android-2895c95a8fb5a6cf";
}
lease 10.3.1.184 {
  starts 4 2014/02/27 02:33:55;
  ends 4 2014/02/27 03:03:55;
  tstp 4 2014/02/27 03:03:55;
  cltt 4 2014/02/27 02:33:55;
  binding state free;
  hardware ethernet 3c:5a:37:2b:9a:76;
  uid "\001<Z7+\232v";
}
lease 10.3.1.64 {
  starts 4 2014/02/27 05:18:29;
  ends 4 2014/02/27 05:48:29;
  tstp 4 2014/02/27 05:48:29;
  cltt 4 2014/02/27 05:18:29;
  binding state free;
  hardware ethernet 04:1b:ba:d8:50:20;
  uid "\001\004\033\272\330P ";
}
lease 10.3.1.77 {
  starts 5 2014/02/28 02:00:43;
  ends 5 2014/02/28 02:30:43;
  tstp 5 2014/02/28 02:30:43;
  cltt 5 2014/02/28 02:00:43;
  binding state free;
  hardware ethernet a4:17:31:48:81:03;
  uid "\001\244\0271H\201\003";
}
lease 10.3.1.76 {
  starts 5 2014/02/28 02:45:32;
  ends 5 2014/02/28 03:15:32;
  tstp 5 2014/02/28 03:15:32;
  cltt 5 2014/02/28 02:45:32;
  binding state free;
  hardware ethernet b0:ee:45:a1:ce:07;
}
lease 10.3.1.140 {
  starts 5 2014/02/28 05:55:55;
  ends 5 2014/02/28 06:55:55;
  tstp 5 2014/02/28 06:55:55;
  cltt 5 2014/02/28 05:55:55;
  binding state free;
  hardware ethernet bc:52:b7:2a:dc:d3;
  uid "\001\274R\267*\334\323";
}
lease 10.3.1.196 {
  starts 4 2014/02/20 21:27:42;
  ends 5 2014/02/28 17:27:42;
  tstp 5 2014/02/28 17:27:42;
  cltt 4 2014/02/20 21:27:42;
  binding state free;
  hardware ethernet 40:b3:95:08:ec:bf;
  uid "\001@\263\225\010\354\277";
}
lease 10.3.1.197 {
  starts 4 2014/02/20 22:58:59;
  ends 5 2014/02/28 18:58:59;
  tstp 5 2014/02/28 18:58:59;
  cltt 4 2014/02/20 22:58:59;
  binding state free;
  hardware ethernet 34:51:c9:82:95:62;
  uid "\0014Q\311\202\225b";
}
lease 10.3.1.147 {
  starts 5 2014/02/28 21:53:15;
  ends 5 2014/02/28 22:23:15;
  tstp 5 2014/02/28 22:23:15;
  cltt 5 2014/02/28 21:53:15;
  binding state free;
  hardware ethernet d0:2d:b3:0d:80:cd;
}
lease 10.3.1.81 {
  starts 6 2014/03/01 00:56:15;
  ends 6 2014/03/01 01:26:15;
  tstp 6 2014/03/01 01:26:15;
  cltt 6 2014/03/01 00:56:15;
  binding state free;
  hardware ethernet 78:e8:b6:20:34:ae;
}
lease 10.3.1.202 {
  starts 6 2014/03/01 03:43:07;
  ends 6 2014/03/01 04:13:07;
  tstp 6 2014/03/01 04:13:07;
  cltt 6 2014/03/01 03:43:07;
  binding state free;
  hardware ethernet 34:23:ba:84:8c:5a;
  uid "\0014#\272\204\214Z";
}
lease 10.3.1.84 {
  starts 6 2014/03/01 22:21:38;
  ends 6 2014/03/01 22:51:38;
  tstp 6 2014/03/01 22:51:38;
  cltt 6 2014/03/01 22:21:38;
  binding state free;
  hardware ethernet 78:6a:89:9f:3a:cf;
}
lease 10.3.1.71 {
  starts 0 2014/03/02 00:56:16;
  ends 0 2014/03/02 01:26:16;
  tstp 0 2014/03/02 01:26:16;
  cltt 0 2014/03/02 00:56:16;
  binding state free;
  hardware ethernet 34:4b:50:b6:3b:4d;
}
lease 10.3.1.88 {
  starts 0 2014/03/02 06:36:50;
  ends 0 2014/03/02 07:36:50;
  tstp 0 2014/03/02 07:36:50;
  cltt 0 2014/03/02 06:36:50;
  binding state free;
  hardware ethernet 00:26:bb:88:52:89;
  uid "\001\000&\273\210R\211";
}
lease 10.3.1.87 {
  starts 0 2014/03/02 09:30:22;
  ends 0 2014/03/02 10:00:22;
  tstp 0 2014/03/02 10:00:22;
  cltt 0 2014/03/02 09:30:22;
  binding state free;
  hardware ethernet d4:20:6d:1c:e4:38;
}
lease 10.3.1.222 {
  starts 0 2014/03/02 22:47:29;
  ends 0 2014/03/02 23:47:29;
  tstp 0 2014/03/02 23:47:29;
  cltt 0 2014/03/02 22:47:29;
  binding state free;
  hardware ethernet 00:23:12:05:82:fc;
  uid "\001\000#\022\005\202\374";
}
lease 10.3.1.74 {
  starts 1 2014/03/03 00:45:35;
  ends 1 2014/03/03 01:15:35;
  tstp 1 2014/03/03 01:15:35;
  cltt 1 2014/03/03 00:45:35;
  binding state free;
  hardware ethernet 88:53:2e:12:38:83;
}
lease 10.3.1.223 {
  starts 1 2014/03/03 01:10:46;
  ends 1 2014/03/03 01:40:46;
  tstp 1 2014/03/03 01:40:46;
  cltt 1 2014/03/03 01:10:46;
  binding state free;
  hardware ethernet 04:fe:31:1c:fb:60;
  uid "\001\004\3761\034\373`";
}
lease 10.3.1.94 {
  starts 1 2014/03/03 03:27:41;
  ends 1 2014/03/03 03:57:41;
  tstp 1 2014/03/03 03:57:41;
  cltt 1 2014/03/03 03:27:41;
  binding state free;
  hardware ethernet 00:1e:0b:b7:c6:45;
}
lease 10.3.1.92 {
  starts 1 2014/03/03 03:53:03;
  ends 1 2014/03/03 04:23:03;
  tstp 1 2014/03/03 04:23:03;
  cltt 1 2014/03/03 03:53:03;
  binding state free;
  hardware ethernet 14:fe:b5:ae:69:92;
}
lease 10.3.1.91 {
  starts 1 2014/03/03 04:02:07;
  ends 1 2014/03/03 04:32:07;
  tstp 1 2014/03/03 04:32:07;
  cltt 1 2014/03/03 04:02:07;
  binding state free;
  hardware ethernet 00:0d:5e:42:42:41;
}
lease 10.3.1.104 {
  starts 1 2014/03/03 04:17:21;
  ends 1 2014/03/03 04:47:21;
  tstp 1 2014/03/03 04:47:21;
  cltt 1 2014/03/03 04:17:21;
  binding state free;
  hardware ethernet 90:c1:15:1c:31:4a;
}
lease 10.3.1.69 {
  starts 1 2014/03/03 05:19:48;
  ends 1 2014/03/03 05:49:48;
  tstp 1 2014/03/03 05:49:48;
  cltt 1 2014/03/03 05:19:48;
  binding state free;
  hardware ethernet 04:46:65:26:e5:09;
}
lease 10.3.1.199 {
  starts 1 2014/03/03 07:00:02;
  ends 1 2014/03/03 07:30:02;
  tstp 1 2014/03/03 07:30:02;
  cltt 1 2014/03/03 07:00:02;
  binding state free;
  hardware ethernet 70:f9:27:15:01:ea;
  uid "\001p\371'\025\001\352";
}
lease 10.3.1.97 {
  starts 1 2014/03/03 07:54:19;
  ends 1 2014/03/03 08:24:19;
  tstp 1 2014/03/03 08:24:19;
  cltt 1 2014/03/03 07:54:19;
  binding state free;
  hardware ethernet 40:b0:fa:8b:71:b9;
}
lease 10.3.1.99 {
  starts 1 2014/03/03 07:56:00;
  ends 1 2014/03/03 08:26:00;
  tstp 1 2014/03/03 08:26:00;
  cltt 1 2014/03/03 07:56:00;
  binding state free;
  hardware ethernet 00:a3:0d:00:41:16;
}
lease 10.3.1.98 {
  starts 1 2014/03/03 07:57:32;
  ends 1 2014/03/03 08:27:32;
  tstp 1 2014/03/03 08:27:32;
  cltt 1 2014/03/03 07:57:32;
  binding state free;
  hardware ethernet 50:9f:27:de:22:7f;
}
lease 10.3.1.1 {
  starts 1 2014/03/03 08:39:17;
  ends 1 2014/03/03 09:09:17;
  tstp 1 2014/03/03 09:09:17;
  cltt 1 2014/03/03 08:39:17;
  binding state free;
  hardware ethernet 00:21:5a:24:19:5a;
}
lease 10.3.1.67 {
  starts 1 2014/03/03 19:30:31;
  ends 1 2014/03/03 20:00:31;
  tstp 1 2014/03/03 20:00:31;
  cltt 1 2014/03/03 19:30:31;
  binding state free;
  hardware ethernet 50:a4:c8:0e:0c:aa;
  uid "\001P\244\310\016\014\252";
}
lease 10.3.1.48 {
  starts 1 2014/03/03 20:10:27;
  ends 1 2014/03/03 20:40:27;
  tstp 1 2014/03/03 20:40:27;
  cltt 1 2014/03/03 20:10:27;
  binding state free;
  hardware ethernet 18:e7:f4:e3:8b:9e;
  uid "\001\030\347\364\343\213\236";
}
lease 10.3.1.3 {
  starts 1 2014/03/03 21:22:21;
  ends 1 2014/03/03 21:52:21;
  tstp 1 2014/03/03 21:52:21;
  cltt 1 2014/03/03 21:22:21;
  binding state free;
  hardware ethernet 00:08:22:86:94:3f;
}
lease 10.3.1.90 {
  starts 1 2014/03/03 21:26:04;
  ends 1 2014/03/03 21:56:04;
  tstp 1 2014/03/03 21:56:04;
  cltt 1 2014/03/03 21:26:04;
  binding state free;
  hardware ethernet 00:7e:0e:03:3b:95;
}
lease 10.3.1.122 {
  starts 1 2014/03/03 22:21:59;
  ends 1 2014/03/03 22:51:59;
  tstp 1 2014/03/03 22:51:59;
  cltt 1 2014/03/03 22:21:59;
  binding state free;
  hardware ethernet 04:46:65:98:77:cc;
  uid "\001\004Fe\230w\314";
}
lease 10.3.1.85 {
  starts 2 2014/03/04 01:28:02;
  ends 2 2014/03/04 01:57:29;
  tstp 2 2014/03/04 01:57:29;
  cltt 2 2014/03/04 01:28:02;
  binding state free;
  hardware ethernet 00:25:56:1b:d4:85;
}
lease 10.3.1.35 {
  starts 2 2014/03/04 03:12:12;
  ends 2 2014/03/04 03:42:12;
  tstp 2 2014/03/04 03:42:12;
  cltt 2 2014/03/04 03:12:12;
  binding state free;
  hardware ethernet 70:05:14:77:7c:54;
}
lease 10.3.1.10 {
  starts 2 2014/03/04 03:25:38;
  ends 2 2014/03/04 03:55:38;
  tstp 2 2014/03/04 03:55:38;
  cltt 2 2014/03/04 03:25:38;
  binding state free;
  hardware ethernet 00:1d:72:0e:1c:e7;
}
lease 10.3.1.9 {
  starts 2 2014/03/04 03:30:17;
  ends 2 2014/03/04 04:00:17;
  tstp 2 2014/03/04 04:00:17;
  cltt 2 2014/03/04 03:30:17;
  binding state free;
  hardware ethernet 00:1d:72:0e:1c:e7;
}
lease 10.3.1.11 {
  starts 2 2014/03/04 03:44:52;
  ends 2 2014/03/04 04:14:52;
  tstp 2 2014/03/04 04:14:52;
  cltt 2 2014/03/04 03:44:52;
  binding state free;
  hardware ethernet 00:17:c4:09:8e:1e;
}
lease 10.3.1.15 {
  starts 2 2014/03/04 06:54:25;
  ends 2 2014/03/04 07:24:25;
  tstp 2 2014/03/04 07:24:25;
  cltt 2 2014/03/04 06:54:25;
  binding state free;
  hardware ethernet c8:d1:5e:32:72:10;
}
lease 10.3.1.17 {
  starts 2 2014/03/04 10:16:44;
  ends 2 2014/03/04 10:46:44;
  tstp 2 2014/03/04 10:46:44;
  cltt 2 2014/03/04 10:16:44;
  binding state free;
  hardware ethernet 00:1b:38:e1:42:f2;
}
lease 10.3.1.146 {
  starts 2 2014/03/04 23:36:50;
  ends 3 2014/03/05 00:06:50;
  tstp 3 2014/03/05 00:06:50;
  cltt 2 2014/03/04 23:36:50;
  binding state free;
  hardware ethernet 08:00:27:6a:c6:94;
  uid "\001\010\000'j\306\224";
}
lease 10.3.1.105 {
  starts 3 2014/03/05 00:33:56;
  ends 3 2014/03/05 01:03:56;
  tstp 3 2014/03/05 01:03:56;
  cltt 3 2014/03/05 00:33:56;
  binding state free;
  hardware ethernet 40:a6:d9:e3:cb:08;
  uid "\001@\246\331\343\313\010";
}
lease 10.3.1.73 {
  starts 3 2014/03/05 01:30:58;
  ends 3 2014/03/05 02:00:58;
  tstp 3 2014/03/05 02:00:58;
  cltt 3 2014/03/05 01:30:58;
  binding state free;
  hardware ethernet 00:07:00:01:73:3d;
}
lease 10.3.1.167 {
  starts 3 2014/03/05 02:49:33;
  ends 3 2014/03/05 03:19:33;
  tstp 3 2014/03/05 03:19:33;
  cltt 3 2014/03/05 02:49:33;
  binding state free;
  hardware ethernet 88:f4:88:2b:92:79;
}
lease 10.3.1.20 {
  starts 3 2014/03/05 04:56:43;
  ends 3 2014/03/05 05:56:43;
  tstp 3 2014/03/05 05:56:43;
  cltt 3 2014/03/05 04:56:43;
  binding state free;
  hardware ethernet 00:25:00:07:f0:dc;
  uid "\001\000%\000\007\360\334";
}
lease 10.3.1.218 {
  starts 3 2014/03/05 05:59:11;
  ends 3 2014/03/05 06:29:11;
  tstp 3 2014/03/05 06:29:11;
  cltt 3 2014/03/05 05:59:11;
  binding state free;
  hardware ethernet e0:b2:f1:3f:b8:28;
}
lease 10.3.1.163 {
  starts 3 2014/03/05 06:21:56;
  ends 3 2014/03/05 06:51:56;
  tstp 3 2014/03/05 06:51:56;
  cltt 3 2014/03/05 06:21:56;
  binding state free;
  hardware ethernet 90:5f:2e:91:9a:16;
}
lease 10.3.1.116 {
  starts 3 2014/03/05 07:01:26;
  ends 3 2014/03/05 07:31:26;
  tstp 3 2014/03/05 07:31:26;
  cltt 3 2014/03/05 07:01:26;
  binding state free;
  hardware ethernet 00:1f:3b:76:ec:bd;
}
lease 10.3.1.42 {
  starts 3 2014/03/05 07:23:27;
  ends 3 2014/03/05 07:53:27;
  tstp 3 2014/03/05 07:53:27;
  cltt 3 2014/03/05 07:23:27;
  binding state free;
  hardware ethernet 00:1a:73:ec:a7:63;
  uid "\001\000\032s\354\247c";
}
lease 10.3.1.136 {
  starts 3 2014/03/05 06:57:36;
  ends 3 2014/03/05 07:57:36;
  tstp 3 2014/03/05 07:57:36;
  cltt 3 2014/03/05 06:57:36;
  binding state free;
  hardware ethernet 14:10:9f:5e:df:10;
  uid "\001\024\020\237^\337\020";
}
lease 10.3.1.39 {
  starts 3 2014/03/05 07:35:25;
  ends 3 2014/03/05 08:05:25;
  tstp 3 2014/03/05 08:05:25;
  cltt 3 2014/03/05 07:35:25;
  binding state free;
  hardware ethernet 00:21:00:1e:02:3c;
  uid "\001\000!\000\036\002<";
}
lease 10.3.1.124 {
  starts 3 2014/03/05 08:52:15;
  ends 3 2014/03/05 09:22:15;
  tstp 3 2014/03/05 09:22:15;
  cltt 3 2014/03/05 08:52:15;
  binding state free;
  hardware ethernet 0c:bd:51:13:1c:c4;
}
lease 10.3.1.106 {
  starts 3 2014/03/05 19:36:52;
  ends 3 2014/03/05 20:06:52;
  tstp 3 2014/03/05 20:06:52;
  cltt 3 2014/03/05 19:36:52;
  binding state free;
  hardware ethernet 30:39:26:8f:f7:3f;
}
lease 10.3.1.115 {
  starts 3 2014/03/05 19:37:01;
  ends 3 2014/03/05 20:07:01;
  tstp 3 2014/03/05 20:07:01;
  cltt 3 2014/03/05 19:37:01;
  binding state free;
  hardware ethernet 9c:02:98:ec:93:05;
  uid "\001\234\002\230\354\223\005";
}
lease 10.3.1.246 {
  starts 3 2014/03/05 22:47:58;
  ends 3 2014/03/05 23:17:58;
  tstp 3 2014/03/05 23:17:58;
  cltt 3 2014/03/05 22:47:58;
  binding state free;
  hardware ethernet 5c:0a:5b:2a:7c:f6;
  uid "\001\\\012[*|\366";
}
lease 10.3.1.112 {
  starts 4 2014/03/06 01:11:05;
  ends 4 2014/03/06 01:41:05;
  tstp 4 2014/03/06 01:41:05;
  cltt 4 2014/03/06 01:11:05;
  binding state free;
  hardware ethernet dc:ce:bc:80:c7:cb;
}
lease 10.3.1.162 {
  starts 4 2014/03/06 01:47:00;
  ends 4 2014/03/06 02:17:00;
  tstp 4 2014/03/06 02:17:00;
  cltt 4 2014/03/06 01:47:00;
  binding state free;
  hardware ethernet e4:2d:02:08:80:65;
}
lease 10.3.1.78 {
  starts 4 2014/03/06 02:33:09;
  ends 4 2014/03/06 03:03:09;
  tstp 4 2014/03/06 03:03:09;
  cltt 4 2014/03/06 02:33:09;
  binding state free;
  hardware ethernet 00:c6:10:ed:9d:f6;
  uid "\001\000\306\020\355\235\366";
}
lease 10.3.1.72 {
  starts 4 2014/03/06 02:36:48;
  ends 4 2014/03/06 03:06:48;
  tstp 4 2014/03/06 03:06:48;
  cltt 4 2014/03/06 02:36:48;
  binding state free;
  hardware ethernet 94:63:d1:5a:ed:bd;
}
lease 10.3.1.119 {
  starts 4 2014/03/06 03:36:18;
  ends 4 2014/03/06 04:06:18;
  tstp 4 2014/03/06 04:06:18;
  cltt 4 2014/03/06 03:36:18;
  binding state free;
  hardware ethernet 90:00:4e:6f:f1:56;
  uid "\001\220\000No\361V";
}
lease 10.3.1.109 {
  starts 4 2014/03/06 03:57:41;
  ends 4 2014/03/06 04:18:41;
  tstp 4 2014/03/06 04:18:41;
  cltt 4 2014/03/06 03:57:41;
  binding state free;
  hardware ethernet 8c:c5:e1:05:0a:b7;
}
lease 10.3.1.95 {
  starts 4 2014/03/06 04:11:47;
  ends 4 2014/03/06 04:41:47;
  tstp 4 2014/03/06 04:41:47;
  cltt 4 2014/03/06 04:11:47;
  binding state free;
  hardware ethernet 00:1e:0b:b0:2b:a3;
}
lease 10.3.1.55 {
  starts 4 2014/03/06 04:11:50;
  ends 4 2014/03/06 04:41:50;
  tstp 4 2014/03/06 04:41:50;
  cltt 4 2014/03/06 04:11:50;
  binding state free;
  hardware ethernet 00:1f:3a:bb:97:22;
}
lease 10.3.1.145 {
  starts 4 2014/03/06 04:22:28;
  ends 4 2014/03/06 04:52:28;
  tstp 4 2014/03/06 04:52:28;
  cltt 4 2014/03/06 04:22:28;
  binding state free;
  hardware ethernet 4c:0b:3a:82:07:23;
}
lease 10.3.1.19 {
  starts 4 2014/03/06 20:25:35;
  ends 4 2014/03/06 20:55:35;
  tstp 4 2014/03/06 20:55:35;
  cltt 4 2014/03/06 20:25:35;
  binding state free;
  hardware ethernet 00:aa:70:a8:1e:75;
}
lease 10.3.1.83 {
  starts 4 2014/03/06 23:00:34;
  ends 4 2014/03/06 23:30:34;
  tstp 4 2014/03/06 23:30:34;
  cltt 4 2014/03/06 23:00:34;
  binding state free;
  hardware ethernet a4:17:31:26:6e:4b;
  uid "\001\244\0271&nK";
}
lease 10.3.1.195 {
  starts 4 2014/03/06 23:27:10;
  ends 5 2014/03/07 00:27:10;
  tstp 5 2014/03/07 00:27:10;
  cltt 4 2014/03/06 23:27:10;
  binding state free;
  hardware ethernet 60:c5:47:d0:af:5f;
  uid "\001`\305G\320\257_";
}
lease 10.3.1.133 {
  starts 5 2014/03/07 02:12:23;
  ends 5 2014/03/07 02:19:50;
  tstp 5 2014/03/07 02:19:50;
  cltt 5 2014/03/07 02:12:23;
  binding state free;
  hardware ethernet 00:21:5a:24:19:5c;
}
lease 10.3.1.110 {
  starts 5 2014/03/07 02:34:38;
  ends 5 2014/03/07 02:38:16;
  tstp 5 2014/03/07 02:38:16;
  cltt 5 2014/03/07 02:34:38;
  binding state free;
  hardware ethernet 00:1e:0b:b0:2b:a3;
}
lease 10.3.1.32 {
  starts 5 2014/03/07 02:26:00;
  ends 5 2014/03/07 02:56:00;
  tstp 5 2014/03/07 02:56:00;
  cltt 5 2014/03/07 02:26:00;
  binding state free;
  hardware ethernet e0:b2:f1:8b:29:ff;
}
lease 10.3.1.111 {
  starts 5 2014/03/07 02:52:20;
  ends 5 2014/03/07 03:00:25;
  tstp 5 2014/03/07 03:00:25;
  cltt 5 2014/03/07 02:52:20;
  binding state free;
  hardware ethernet 00:1f:29:50:22:a5;
}
lease 10.3.1.43 {
  starts 5 2014/03/07 02:33:16;
  ends 5 2014/03/07 03:03:16;
  tstp 5 2014/03/07 03:03:16;
  cltt 5 2014/03/07 02:33:16;
  binding state free;
  hardware ethernet b0:c4:e7:71:7a:8f;
  uid "\001\260\304\347qz\217";
}
lease 10.3.1.108 {
  starts 5 2014/03/07 03:00:24;
  ends 5 2014/03/07 03:30:24;
  tstp 5 2014/03/07 03:30:24;
  cltt 5 2014/03/07 03:00:24;
  binding state free;
  hardware ethernet e4:2d:02:80:0b:59;
}
lease 10.3.1.45 {
  starts 5 2014/03/07 03:05:09;
  ends 5 2014/03/07 03:35:09;
  tstp 5 2014/03/07 03:35:09;
  cltt 5 2014/03/07 03:05:09;
  binding state free;
  hardware ethernet 00:66:4b:bb:76:d2;
}
lease 10.3.1.18 {
  starts 5 2014/03/07 05:08:45;
  ends 5 2014/03/07 05:23:01;
  tstp 5 2014/03/07 05:23:01;
  cltt 5 2014/03/07 05:08:45;
  binding state free;
  hardware ethernet 0c:37:dc:93:26:89;
}
lease 10.3.1.252 {
  starts 5 2014/03/07 06:57:26;
  ends 5 2014/03/07 07:27:26;
  tstp 5 2014/03/07 07:27:26;
  cltt 5 2014/03/07 06:57:26;
  binding state free;
  hardware ethernet 78:47:1d:72:6a:2c;
  uid "\001xG\035rj,";
}
lease 10.3.1.113 {
  starts 5 2014/03/07 07:46:22;
  ends 5 2014/03/07 08:46:22;
  tstp 5 2014/03/07 08:46:22;
  cltt 5 2014/03/07 07:46:22;
  binding state free;
  hardware ethernet e4:ce:8f:ec:c8:f2;
  uid "\001\344\316\217\354\310\362";
}
lease 10.3.1.80 {
  starts 5 2014/03/07 20:00:54;
  ends 5 2014/03/07 20:30:54;
  tstp 5 2014/03/07 20:30:54;
  cltt 5 2014/03/07 20:00:54;
  binding state free;
  hardware ethernet 0c:bd:51:15:72:e4;
}
lease 10.3.1.224 {
  starts 5 2014/03/07 21:52:05;
  ends 5 2014/03/07 22:22:05;
  tstp 5 2014/03/07 22:22:05;
  cltt 5 2014/03/07 21:52:05;
  binding state free;
  hardware ethernet c8:19:f7:3a:15:4b;
  uid "\001\310\031\367:\025K";
}
lease 10.3.1.12 {
  starts 5 2014/03/07 23:02:28;
  ends 5 2014/03/07 23:32:28;
  tstp 5 2014/03/07 23:32:28;
  cltt 5 2014/03/07 23:02:28;
  binding state free;
  hardware ethernet 80:96:b1:1c:3d:07;
}
lease 10.3.1.16 {
  starts 5 2014/03/07 23:08:06;
  ends 5 2014/03/07 23:38:06;
  tstp 5 2014/03/07 23:38:06;
  cltt 5 2014/03/07 23:08:06;
  binding state free;
  hardware ethernet d0:2d:b3:0c:b4:c0;
}
lease 10.3.1.89 {
  starts 6 2014/03/08 00:42:17;
  ends 6 2014/03/08 01:12:17;
  tstp 6 2014/03/08 01:12:17;
  cltt 6 2014/03/08 00:42:17;
  binding state free;
  hardware ethernet e4:2d:02:6d:79:c7;
}
lease 10.3.1.123 {
  starts 6 2014/03/08 02:31:31;
  ends 6 2014/03/08 03:31:31;
  tstp 6 2014/03/08 03:31:31;
  cltt 6 2014/03/08 02:31:31;
  binding state free;
  hardware ethernet 70:73:cb:9d:b1:eb;
  uid "\001ps\313\235\261\353";
}
lease 10.3.1.5 {
  starts 6 2014/03/08 06:03:36;
  ends 6 2014/03/08 06:33:36;
  tstp 6 2014/03/08 06:33:36;
  cltt 6 2014/03/08 06:03:36;
  binding state free;
  hardware ethernet 8c:c5:e1:02:bc:ff;
}
lease 10.3.1.179 {
  starts 6 2014/03/08 08:11:56;
  ends 6 2014/03/08 08:41:56;
  tstp 6 2014/03/08 08:41:56;
  cltt 6 2014/03/08 08:11:56;
  binding state free;
  hardware ethernet c0:f8:da:3e:6b:34;
  uid "\001\300\370\332>k4";
}
lease 10.3.1.132 {
  starts 6 2014/03/08 21:46:47;
  ends 6 2014/03/08 22:16:47;
  tstp 6 2014/03/08 22:16:47;
  cltt 6 2014/03/08 21:46:47;
  binding state free;
  hardware ethernet 9c:b7:0d:96:5d:fa;
  uid "\001\234\267\015\226]\372";
}
lease 10.3.1.135 {
  starts 6 2014/03/08 21:57:02;
  ends 6 2014/03/08 22:27:02;
  tstp 6 2014/03/08 22:27:02;
  cltt 6 2014/03/08 21:57:02;
  binding state free;
  hardware ethernet 78:e8:b6:a6:2b:37;
}
lease 10.3.1.216 {
  starts 6 2014/03/08 22:49:31;
  ends 6 2014/03/08 23:19:31;
  tstp 6 2014/03/08 23:19:31;
  cltt 6 2014/03/08 22:49:31;
  binding state free;
  hardware ethernet b8:5e:7b:8b:df:17;
  uid "\001\270^{\213\337\027";
}
lease 10.3.1.189 {
  starts 0 2014/03/09 00:31:59;
  ends 0 2014/03/09 01:01:59;
  tstp 0 2014/03/09 01:01:59;
  cltt 0 2014/03/09 00:31:59;
  binding state free;
  hardware ethernet b8:5e:7b:83:2b:10;
  uid "\001\270^{\203+\020";
}
lease 10.3.1.82 {
  starts 0 2014/03/09 01:16:13;
  ends 0 2014/03/09 01:46:13;
  tstp 0 2014/03/09 01:46:13;
  cltt 0 2014/03/09 01:16:13;
  binding state free;
  hardware ethernet 0c:14:20:96:e6:c2;
  uid "\001\014\024 \226\346\302";
}
lease 10.3.1.8 {
  starts 0 2014/03/09 01:53:36;
  ends 0 2014/03/09 02:23:36;
  tstp 0 2014/03/09 02:23:36;
  cltt 0 2014/03/09 01:53:36;
  binding state free;
  hardware ethernet bc:cf:cc:a0:5d:2f;
  uid "\001\274\317\314\240]/";
}
lease 10.3.1.6 {
  starts 0 2014/03/09 01:24:14;
  ends 0 2014/03/09 02:24:14;
  tstp 0 2014/03/09 02:24:14;
  cltt 0 2014/03/09 01:24:14;
  binding state free;
  hardware ethernet d8:d1:cb:49:83:a3;
  uid "\001\330\321\313I\203\243";
}
lease 10.3.1.141 {
  starts 0 2014/03/09 02:46:21;
  ends 0 2014/03/09 03:16:21;
  tstp 0 2014/03/09 03:16:21;
  cltt 0 2014/03/09 02:46:21;
  binding state free;
  hardware ethernet 3c:df:bd:33:87:6b;
}
lease 10.3.1.143 {
  starts 0 2014/03/09 02:49:20;
  ends 0 2014/03/09 03:19:20;
  tstp 0 2014/03/09 03:19:20;
  cltt 0 2014/03/09 02:49:20;
  binding state free;
  hardware ethernet d0:2d:b3:95:6b:fe;
}
lease 10.3.1.206 {
  starts 0 2014/03/09 03:31:57;
  ends 0 2014/03/09 04:01:57;
  tstp 0 2014/03/09 04:01:57;
  cltt 0 2014/03/09 03:31:57;
  binding state free;
  hardware ethernet e4:40:e2:30:3d:e8;
  uid "\001\344@\3420=\350";
}
lease 10.3.1.165 {
  starts 0 2014/03/09 03:29:35;
  ends 0 2014/03/09 04:29:35;
  tstp 0 2014/03/09 04:29:35;
  cltt 0 2014/03/09 03:29:35;
  binding state free;
  hardware ethernet c4:2c:03:73:58:b4;
  uid "\001\304,\003sX\264";
}
lease 10.3.1.148 {
  starts 0 2014/03/09 04:27:18;
  ends 0 2014/03/09 05:27:18;
  tstp 0 2014/03/09 05:27:18;
  cltt 0 2014/03/09 04:27:18;
  binding state free;
  hardware ethernet 60:33:4b:62:8b:f4;
  uid "\001`3Kb\213\364";
}
lease 10.3.1.142 {
  starts 0 2014/03/09 05:03:51;
  ends 0 2014/03/09 05:33:51;
  tstp 0 2014/03/09 05:33:51;
  cltt 0 2014/03/09 05:03:51;
  binding state free;
  hardware ethernet 64:77:91:43:f2:3e;
  uid "\001dw\221C\362>";
}
lease 10.3.1.118 {
  starts 0 2014/03/09 05:05:54;
  ends 0 2014/03/09 05:35:54;
  tstp 0 2014/03/09 05:35:54;
  cltt 0 2014/03/09 05:05:54;
  binding state free;
  hardware ethernet 70:f9:27:a5:fe:38;
  uid "\001p\371'\245\3768";
}
lease 10.3.1.117 {
  starts 0 2014/03/09 05:20:36;
  ends 0 2014/03/09 05:50:36;
  tstp 0 2014/03/09 05:50:36;
  cltt 0 2014/03/09 05:20:36;
  binding state free;
  hardware ethernet d0:e7:82:fc:1f:73;
}
lease 10.3.1.86 {
  starts 0 2014/03/09 05:26:24;
  ends 0 2014/03/09 05:56:24;
  tstp 0 2014/03/09 05:56:24;
  cltt 0 2014/03/09 05:26:24;
  binding state free;
  hardware ethernet f4:55:9c:6c:5f:06;
}
lease 10.3.1.13 {
  starts 0 2014/03/09 05:27:02;
  ends 0 2014/03/09 05:57:02;
  tstp 0 2014/03/09 05:57:02;
  cltt 0 2014/03/09 05:27:02;
  binding state free;
  hardware ethernet 84:51:81:c3:ce:60;
  uid "\001\204Q\201\303\316`";
}
lease 10.3.1.130 {
  starts 0 2014/03/09 05:48:08;
  ends 0 2014/03/09 06:17:49;
  tstp 0 2014/03/09 06:17:49;
  cltt 0 2014/03/09 05:48:08;
  binding state free;
  hardware ethernet 48:a2:2d:26:87:65;
}
lease 10.3.1.150 {
  starts 0 2014/03/09 05:55:56;
  ends 0 2014/03/09 06:25:56;
  tstp 0 2014/03/09 06:25:56;
  cltt 0 2014/03/09 05:55:56;
  binding state free;
  hardware ethernet 34:c0:59:95:3a:fd;
  uid "\0014\300Y\225:\375";
}
lease 10.3.1.61 {
  starts 0 2014/03/09 05:58:16;
  ends 0 2014/03/09 06:28:16;
  tstp 0 2014/03/09 06:28:16;
  cltt 0 2014/03/09 05:58:16;
  binding state free;
  hardware ethernet 00:26:e8:42:20:12;
  uid "\001\000&\350B \022";
}
lease 10.3.1.51 {
  starts 0 2014/03/09 06:02:26;
  ends 0 2014/03/09 06:32:26;
  tstp 0 2014/03/09 06:32:26;
  cltt 0 2014/03/09 06:02:26;
  binding state free;
  hardware ethernet 0c:71:5d:4a:d6:e3;
  uid "\001\014q]J\326\343";
}
lease 10.3.1.151 {
  starts 0 2014/03/09 06:18:46;
  ends 0 2014/03/09 06:48:46;
  tstp 0 2014/03/09 06:48:46;
  cltt 0 2014/03/09 06:18:46;
  binding state free;
  hardware ethernet 40:b0:fa:b2:08:17;
}
lease 10.3.1.79 {
  starts 0 2014/03/09 06:23:32;
  ends 0 2014/03/09 06:53:32;
  tstp 0 2014/03/09 06:53:32;
  cltt 0 2014/03/09 06:23:32;
  binding state free;
  hardware ethernet 2c:44:01:6c:26:3a;
  uid "\001,D\001l&:";
}
lease 10.3.1.2 {
  starts 0 2014/03/09 06:40:54;
  ends 0 2014/03/09 07:10:54;
  tstp 0 2014/03/09 07:10:54;
  cltt 0 2014/03/09 06:40:54;
  binding state free;
  hardware ethernet bc:f5:ac:a2:6d:8c;
}
lease 10.3.1.21 {
  starts 0 2014/03/09 07:03:00;
  ends 0 2014/03/09 07:33:00;
  tstp 0 2014/03/09 07:33:00;
  cltt 0 2014/03/09 07:03:00;
  binding state free;
  hardware ethernet 98:e7:9a:10:83:f5;
}
lease 10.3.1.4 {
  starts 0 2014/03/09 07:10:33;
  ends 0 2014/03/09 07:40:33;
  tstp 0 2014/03/09 07:40:33;
  cltt 0 2014/03/09 07:10:33;
  binding state free;
  hardware ethernet 48:d2:24:1f:b5:d2;
  uid "\001H\322$\037\265\322";
}
lease 10.3.1.169 {
  starts 0 2014/03/09 08:27:06;
  ends 0 2014/03/09 08:57:06;
  tstp 0 2014/03/09 08:57:06;
  cltt 0 2014/03/09 08:27:06;
  binding state free;
  hardware ethernet 00:1d:e0:30:52:f5;
  uid "\001\000\035\3400R\365";
}
lease 10.3.1.70 {
  starts 0 2014/03/09 09:05:02;
  ends 0 2014/03/09 09:35:02;
  tstp 0 2014/03/09 09:35:02;
  cltt 0 2014/03/09 09:05:02;
  binding state free;
  hardware ethernet 0c:bd:51:0c:93:ba;
}
lease 10.3.1.180 {
  starts 0 2014/03/09 19:33:44;
  ends 0 2014/03/09 19:35:44;
  cltt 0 2014/03/09 19:33:44;
  binding state free;
  hardware ethernet 4c:0b:3a:8d:af:4e;
  uid "\001L\013:\215\257N";
}
lease 10.3.1.187 {
  starts 0 2014/03/09 19:11:58;
  ends 0 2014/03/09 19:41:58;
  tstp 0 2014/03/09 19:41:58;
  cltt 0 2014/03/09 19:11:58;
  binding state free;
  hardware ethernet e4:2d:02:c2:a9:2b;
}
lease 10.3.1.221 {
  starts 0 2014/03/09 19:16:24;
  ends 0 2014/03/09 19:44:22;
  tstp 0 2014/03/09 19:44:22;
  cltt 0 2014/03/09 19:16:24;
  binding state free;
  hardware ethernet 00:24:9f:71:79:0f;
  uid "\001\000$\237qy\017";
}
lease 10.3.1.164 {
  starts 0 2014/03/09 20:00:38;
  ends 0 2014/03/09 20:30:38;
  tstp 0 2014/03/09 20:30:38;
  cltt 0 2014/03/09 20:00:38;
  binding state free;
  hardware ethernet 88:30:8a:e6:d6:41;
  uid "\001\2100\212\346\326A";
}
lease 10.3.1.238 {
  starts 1 2014/03/10 00:10:52;
  ends 1 2014/03/10 00:40:52;
  tstp 1 2014/03/10 00:40:52;
  cltt 1 2014/03/10 00:10:52;
  binding state free;
  hardware ethernet 20:7c:8f:80:f8:a1;
  uid "\001 |\217\200\370\241";
}
lease 10.3.1.160 {
  starts 1 2014/03/10 00:33:59;
  ends 1 2014/03/10 01:03:59;
  tstp 1 2014/03/10 01:03:59;
  cltt 1 2014/03/10 00:33:59;
  binding state free;
  hardware ethernet 00:1f:3c:54:2c:d9;
}
lease 10.3.1.153 {
  starts 1 2014/03/10 00:44:04;
  ends 1 2014/03/10 01:14:04;
  tstp 1 2014/03/10 01:14:04;
  cltt 1 2014/03/10 00:44:04;
  binding state free;
  hardware ethernet 78:d6:f0:ed:74:da;
  uid "\001x\326\360\355t\332";
}
lease 10.3.1.247 {
  starts 1 2014/03/10 00:46:09;
  ends 1 2014/03/10 01:16:09;
  tstp 1 2014/03/10 01:16:09;
  cltt 1 2014/03/10 00:46:09;
  binding state free;
  hardware ethernet 14:10:9f:70:2d:56;
  uid "\001\024\020\237p-V";
}
lease 10.3.1.200 {
  starts 1 2014/03/10 00:59:15;
  ends 1 2014/03/10 01:29:15;
  cltt 1 2014/03/10 00:59:15;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 1c:3e:84:7d:69:0d;
  uid "\001\034>\204}i\015";
  client-hostname "Fardowsa";
}
lease 10.3.1.253 {
  starts 1 2014/03/10 01:05:04;
  ends 1 2014/03/10 01:35:04;
  cltt 1 2014/03/10 01:05:04;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet c0:18:85:4d:61:3f;
  uid "\001\300\030\205Ma?";
  client-hostname "AcerOne-PC";
}
lease 10.3.1.40 {
  starts 1 2014/03/10 01:12:04;
  ends 1 2014/03/10 01:42:04;
  cltt 1 2014/03/10 01:12:04;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 08:60:6e:a3:7d:19;
  uid "\001\010`n\243}\031";
  client-hostname "android-f0851122b7ea6e7f";
}
lease 10.3.1.101 {
  starts 1 2014/03/10 01:12:05;
  ends 1 2014/03/10 01:42:05;
  cltt 1 2014/03/10 01:12:05;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:37:6d:27:69:ed;
  client-hostname "android_431478b1f9238843";
}
lease 10.3.1.239 {
  starts 1 2014/03/10 01:12:40;
  ends 1 2014/03/10 01:42:40;
  cltt 1 2014/03/10 01:12:40;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:0e:35:dc:4c:58;
  uid "\001\000\0165\334LX";
  client-hostname "thinkpad";
}
lease 10.3.1.158 {
  starts 1 2014/03/10 01:13:18;
  ends 1 2014/03/10 01:43:18;
  cltt 1 2014/03/10 01:13:18;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet c4:62:ea:85:55:59;
  uid "\001\304b\352\205UY";
  client-hostname "android-ffb40a6bd59978fd";
}
lease 10.3.1.154 {
  starts 1 2014/03/10 01:16:40;
  ends 1 2014/03/10 01:46:40;
  cltt 1 2014/03/10 01:16:40;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 28:0d:fc:70:97:51;
  uid "\001(\015\374p\227Q";
}
lease 10.3.1.96 {
  starts 1 2014/03/10 01:18:33;
  ends 1 2014/03/10 01:48:33;
  cltt 1 2014/03/10 01:18:33;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 50:9f:27:de:1c:12;
  client-hostname "android-59be0efb3a34af8e";
}
lease 10.3.1.156 {
  starts 1 2014/03/10 01:24:44;
  ends 1 2014/03/10 01:54:44;
  cltt 1 2014/03/10 01:24:44;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet b8:5e:7b:83:10:f2;
  uid "\001\270^{\203\020\362";
  client-hostname "android-f174910ebbb47b3";
}
lease 10.3.1.159 {
  starts 1 2014/03/10 01:25:13;
  ends 1 2014/03/10 01:55:13;
  cltt 1 2014/03/10 01:25:13;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:40:8c:97:e0:42;
  uid "\001\000@\214\227\340B";
  client-hostname "axis-00408c97e042";
}
lease 10.3.1.155 {
  starts 1 2014/03/10 01:26:06;
  ends 1 2014/03/10 01:56:06;
  cltt 1 2014/03/10 01:26:06;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 08:d4:2b:f2:b0:77;
  uid "\001\010\324+\362\260w";
}
lease 10.3.1.93 {
  starts 1 2014/03/10 01:26:37;
  ends 1 2014/03/10 01:56:37;
  cltt 1 2014/03/10 01:26:37;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:1e:0b:b5:1f:52;
  client-hostname "figlet";
}
lease 10.2.1.3 {
  starts 6 2014/01/25 00:12:29;
  ends 0 2014/01/26 00:12:29;
  tstp 0 2014/01/26 00:12:29;
  cltt 6 2014/01/25 00:12:29;
  binding state free;
  hardware ethernet 00:22:64:ad:3f:5b;
  uid "\001\000\"d\255?[";
}
lease 10.2.1.5 {
  starts 6 2014/01/25 00:45:24;
  ends 0 2014/01/26 00:45:24;
  tstp 0 2014/01/26 00:45:24;
  cltt 6 2014/01/25 00:45:24;
  binding state free;
  hardware ethernet 00:22:64:ad:3f:5b;
}
lease 10.2.1.31 {
  starts 5 2014/02/14 22:31:05;
  ends 5 2014/02/14 22:47:02;
  tstp 5 2014/02/14 22:47:02;
  cltt 5 2014/02/14 22:31:05;
  binding state free;
  hardware ethernet 00:1e:68:75:88:e3;
}
lease 10.2.1.6 {
  starts 5 2014/02/14 21:25:15;
  ends 6 2014/02/15 21:25:15;
  tstp 6 2014/02/15 21:25:15;
  cltt 5 2014/02/14 21:25:15;
  binding state free;
  hardware ethernet 00:15:c5:a6:7c:06;
}
lease 10.2.1.27 {
  starts 5 2014/02/14 21:26:39;
  ends 6 2014/02/15 21:26:39;
  tstp 6 2014/02/15 21:26:39;
  cltt 5 2014/02/14 21:26:39;
  binding state free;
  hardware ethernet 00:11:11:f1:8b:59;
  uid "\001\000\021\021\361\213Y";
}
lease 10.2.1.26 {
  starts 5 2014/02/14 21:49:52;
  ends 6 2014/02/15 21:49:52;
  tstp 6 2014/02/15 21:49:52;
  cltt 5 2014/02/14 21:49:52;
  binding state free;
  hardware ethernet 00:1b:fc:3e:fa:81;
  uid "\001\000\033\374>\372\201";
}
lease 10.2.1.30 {
  starts 5 2014/02/14 22:03:47;
  ends 6 2014/02/15 22:03:47;
  tstp 6 2014/02/15 22:03:47;
  cltt 5 2014/02/14 22:03:47;
  binding state free;
  hardware ethernet 20:cf:30:0c:03:15;
  uid "\001 \3170\014\003\025";
}
lease 10.2.1.29 {
  starts 5 2014/02/14 22:14:31;
  ends 6 2014/02/15 22:14:31;
  tstp 6 2014/02/15 22:14:31;
  cltt 5 2014/02/14 22:14:31;
  binding state free;
  hardware ethernet 00:1b:fc:3e:fa:81;
}
lease 10.2.1.28 {
  starts 6 2014/02/15 00:02:03;
  ends 0 2014/02/16 00:02:03;
  tstp 0 2014/02/16 00:02:03;
  cltt 6 2014/02/15 00:02:03;
  binding state free;
  hardware ethernet 00:26:18:4a:00:72;
}
lease 10.2.1.32 {
  starts 6 2014/02/15 02:13:46;
  ends 0 2014/02/16 02:13:46;
  tstp 0 2014/02/16 02:13:46;
  cltt 6 2014/02/15 02:13:46;
  binding state free;
  hardware ethernet b8:27:eb:ef:cb:25;
  uid "xbmc-cb25";
}
lease 10.2.1.33 {
  starts 6 2014/02/15 02:48:49;
  ends 0 2014/02/16 02:48:49;
  tstp 0 2014/02/16 02:48:49;
  cltt 6 2014/02/15 02:48:49;
  binding state free;
  hardware ethernet 00:1a:a0:98:bc:b7;
  uid "\001\000\032\240\230\274\267";
}
lease 10.2.1.34 {
  starts 6 2014/02/15 03:06:19;
  ends 0 2014/02/16 03:06:19;
  tstp 0 2014/02/16 03:06:19;
  cltt 6 2014/02/15 03:06:19;
  binding state free;
  hardware ethernet 00:11:25:45:91:03;
}
lease 10.2.1.2 {
  starts 5 2014/02/21 23:30:40;
  ends 6 2014/02/22 23:30:40;
  tstp 6 2014/02/22 23:30:40;
  cltt 5 2014/02/21 23:30:40;
  binding state free;
  hardware ethernet 00:13:d3:ce:e5:a0;
  uid "\001\000\023\323\316\345\240";
}
lease 10.2.1.35 {
  starts 5 2014/02/28 00:37:09;
  ends 5 2014/02/28 01:07:09;
  tstp 5 2014/02/28 01:07:09;
  cltt 5 2014/02/28 00:37:09;
  binding state free;
  hardware ethernet 00:0d:5e:42:42:41;
  uid "\001\000\015^BBA";
}
lease 10.2.1.36 {
  starts 5 2014/02/28 02:17:06;
  ends 5 2014/02/28 02:47:06;
  tstp 5 2014/02/28 02:47:06;
  cltt 5 2014/02/28 02:17:06;
  binding state free;
  hardware ethernet 00:0d:5e:42:42:41;
}
lease 10.2.1.4 {
  starts 5 2014/02/28 10:39:02;
  ends 5 2014/02/28 11:09:02;
  tstp 5 2014/02/28 11:09:02;
  cltt 5 2014/02/28 10:39:02;
  binding state free;
  hardware ethernet 00:13:d3:ce:e5:a0;
}
lease 10.2.1.25 {
  starts 5 2014/03/07 02:28:42;
  ends 5 2014/03/07 02:58:42;
  tstp 5 2014/03/07 02:58:42;
  cltt 5 2014/03/07 02:28:42;
  binding state free;
  hardware ethernet 00:50:f2:86:8a:e2;
  uid "\001\000P\362\206\212\342";
}
lease 10.2.1.1 {
  starts 1 2014/03/10 01:19:39;
  ends 1 2014/03/10 01:49:39;
  cltt 1 2014/03/10 01:19:39;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:0e:08:ed:8a:55;
  uid "\001\000\016\010\355\212U";
  client-hostname "SipuraSPA";
}
server-duid "\000\001\000\001\032d\300\261\000\023\367\032p\237";

lease 10.3.1.8 {
  starts 1 2014/03/10 01:27:03;
  ends 1 2014/03/10 01:27:03;
  cltt 1 2014/03/10 01:27:03;
  binding state abandoned;
  next binding state free;
  rewind binding state free;
  client-hostname "android-d3420db891b9ada6";
}
lease 10.3.1.128 {
  starts 1 2014/03/10 01:27:08;
  ends 1 2014/03/10 01:57:08;
  cltt 1 2014/03/10 01:27:08;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet bc:cf:cc:a0:5d:2f;
  uid "\001\274\317\314\240]/";
  client-hostname "android-d3420db891b9ada6";
}
lease 10.3.1.239 {
  starts 1 2014/03/10 01:27:11;
  ends 1 2014/03/10 01:57:11;
  cltt 1 2014/03/10 01:27:11;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:0e:35:dc:4c:58;
  uid "\001\000\0165\334LX";
  client-hostname "thinkpad";
}
lease 10.3.1.158 {
  starts 1 2014/03/10 01:27:43;
  ends 1 2014/03/10 01:57:43;
  cltt 1 2014/03/10 01:27:43;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet c4:62:ea:85:55:59;
  uid "\001\304b\352\205UY";
  client-hostname "android-ffb40a6bd59978fd";
}
lease 10.3.1.8 {
  starts 1 2014/03/10 01:27:03;
  ends 1 2014/03/10 01:27:03;
  cltt 1 2014/03/10 01:27:03;
  binding state free;
  client-hostname "android-d3420db891b9ada6";
}
lease 10.3.1.200 {
  starts 1 2014/03/10 00:59:15;
  ends 1 2014/03/10 01:29:15;
  tstp 1 2014/03/10 01:29:15;
  cltt 1 2014/03/10 00:59:15;
  binding state free;
  hardware ethernet 1c:3e:84:7d:69:0d;
  uid "\001\034>\204}i\015";
}
lease 10.3.1.155 {
  starts 1 2014/03/10 01:30:22;
  ends 1 2014/03/10 02:00:22;
  cltt 1 2014/03/10 01:30:22;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 08:d4:2b:f2:b0:77;
  uid "\001\010\324+\362\260w";
}
lease 10.3.1.166 {
  starts 1 2014/03/10 01:30:33;
  ends 1 2014/03/10 02:00:33;
  cltt 1 2014/03/10 01:30:33;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet d8:57:ef:3d:12:d6;
  uid "\001\330W\357=\022\326";
}
lease 10.3.1.154 {
  starts 1 2014/03/10 01:31:40;
  ends 1 2014/03/10 02:01:40;
  cltt 1 2014/03/10 01:31:40;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 28:0d:fc:70:97:51;
  uid "\001(\015\374p\227Q";
}
lease 10.3.1.96 {
  starts 1 2014/03/10 01:32:59;
  ends 1 2014/03/10 02:02:59;
  cltt 1 2014/03/10 01:32:59;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 50:9f:27:de:1c:12;
  client-hostname "android-59be0efb3a34af8e";
}
lease 10.2.1.1 {
  starts 1 2014/03/10 01:34:39;
  ends 1 2014/03/10 02:04:39;
  cltt 1 2014/03/10 01:34:39;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:0e:08:ed:8a:55;
  uid "\001\000\016\010\355\212U";
  client-hostname "SipuraSPA";
}
lease 10.3.1.253 {
  starts 1 2014/03/10 01:05:04;
  ends 1 2014/03/10 01:35:04;
  tstp 1 2014/03/10 01:35:04;
  cltt 1 2014/03/10 01:05:04;
  binding state free;
  hardware ethernet c0:18:85:4d:61:3f;
  uid "\001\300\030\205Ma?";
}
lease 10.3.1.166 {
  starts 1 2014/03/10 01:39:01;
  ends 1 2014/03/10 02:09:01;
  cltt 1 2014/03/10 01:39:01;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet d8:57:ef:3d:12:d6;
  uid "\001\330W\357=\022\326";
}
lease 10.3.1.156 {
  starts 1 2014/03/10 01:39:09;
  ends 1 2014/03/10 02:09:09;
  cltt 1 2014/03/10 01:39:09;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet b8:5e:7b:83:10:f2;
  uid "\001\270^{\203\020\362";
  client-hostname "android-f174910ebbb47b3";
}
lease 10.3.1.159 {
  starts 1 2014/03/10 01:40:14;
  ends 1 2014/03/10 02:10:14;
  cltt 1 2014/03/10 01:40:14;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:40:8c:97:e0:42;
  uid "\001\000@\214\227\340B";
  client-hostname "axis-00408c97e042";
}
lease 10.3.1.93 {
  starts 1 2014/03/10 01:40:14;
  ends 1 2014/03/10 02:10:14;
  cltt 1 2014/03/10 01:40:14;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:1e:0b:b5:1f:52;
  client-hostname "figlet";
}
"""

# <codecell>

# 
# dhcpd_leases_parser.py
#
# Copyright 2008, Paul McGuire
#
# Sample parser to parse a dhcpd.leases file to extract leases 
# and lease attributes
#
# format ref: http://www.linuxmanpages.com/man5/dhcpd.leases.5.php
#

sample = r"""\
# All times in this file are in UTC (GMT), not your local timezone.   This is
# not a bug, so please don't ask about it.   There is no portable way to
# store leases in the local timezone, so please don't request this as a
# feature.   If this is inconvenient or confusing to you, we sincerely
# apologize.   Seriously, though - don't ask.
# The format of this file is documented in the dhcpd.leases(5) manual page.
# This lease file was written by isc-dhcp-V3.0.4

lease 192.168.0.250 {
  starts 3 2008/01/23 17:16:41;
  ends 6 2008/02/02 17:16:41;
  tstp 6 2008/02/02 17:16:41;
  binding state free;
  hardware ethernet 00:17:f2:9b:d8:19;
  uid "\001\000\027\362\233\330\031";
}
lease 192.168.0.198 {
  starts 1 2008/02/04 13:46:55;
  ends never;
  tstp 1 2008/02/04 17:04:14;
  binding state free;
  hardware ethernet 00:13:72:d3:3b:98;
  uid "\001\000\023r\323;\230";
}
lease 10.3.1.93 {
  starts 1 2014/03/10 01:40:14;
  ends 1 2014/03/10 02:10:14;
  cltt 1 2014/03/10 01:40:14;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:1e:0b:b5:1f:52;
  client-hostname "figlet";
}

"""

from pyparsing import *
import datetime,time

LBRACE,RBRACE,SEMI,QUOTE = map(Suppress,'{};"')
ipAddress = Combine(Word(nums) + ('.' + Word(nums))*3)
hexint = Word(hexnums,exact=2)
macAddress = Combine(hexint + (':'+hexint)*5)
hdwType = Word(alphanums)

yyyymmdd = Combine((Word(nums,exact=4)|Word(nums,exact=2))+
                    ('/'+Word(nums,exact=2))*2)
hhmmss = Combine(Word(nums,exact=2)+(':'+Word(nums,exact=2))*2)
dateRef = oneOf(list("0123456"))("weekday") + yyyymmdd("date") + \
                                                        hhmmss("time")

def utcToLocalTime(tokens):
    utctime = datetime.datetime.strptime("%(date)s %(time)s" % tokens,
                                                    "%Y/%m/%d %H:%M:%S")
    localtime = utctime-datetime.timedelta(0,time.timezone,0)
    tokens["utcdate"],tokens["utctime"] = tokens["date"],tokens["time"]
    tokens["localdate"],tokens["localtime"] = str(localtime).split()
    del tokens["date"]
    del tokens["time"]
dateRef.setParseAction(utcToLocalTime)

startsStmt = "starts" + dateRef + SEMI
endsStmt = "ends" + (dateRef | "never") + SEMI
tstpStmt = "tstp" + dateRef + SEMI
tsfpStmt = "tsfp" + dateRef + SEMI
hdwStmt = "hardware" + hdwType("type") + macAddress("mac") + SEMI
uidStmt = "uid" + QuotedString('"')("uid") + SEMI
bindingStmt = "binding" + Word(alphanums) + Word(alphanums) + SEMI

leaseStatement = startsStmt | endsStmt | tstpStmt | tsfpStmt | hdwStmt | \
                                                        uidStmt | bindingStmt
leaseDef = "lease" + ipAddress("ipaddress") + LBRACE + \
                            Dict(ZeroOrMore(Group(leaseStatement))) + RBRACE

for lease in leaseDef.searchString(sample):
    print lease.dump()
    print lease.ipaddress,'->',lease.hardware.mac
    lisbleh.append(lease.ipaddress)
    lisbleh.append(lease.hardware.mac)

# <codecell>

lisbleh

# <codecell>

#!/usr/bin/python3

def split_ip(ip):
    return tuple(int(part) for part in ip.split('.'))

def ip_key(item):
    return split_ip(item[0])

def parse(fileName):

    f = open( fileName, "r" )
    output = {}
    thisIp = ""
    thisMAC = ""
    thisName = ""
    
    for line in f:
        
        # ip
        if (line.find("lease") == 0):
            if (thisIp != ""):
                output[thisIp] = thisIp + " " + thisMAC + " " + thisName
                thisMAC = ""
                thisName = ""
                
            thisIp = line[line.find(" ") +1 : line.find("{") -1]

        # mac
        if(line.find("hardware ethernet") > -1):
            thisMAC = line[line.find("ethernet") +9 : line.find(";")]
        
        # uid - will be replaced with name if it exists
        if(line.find("uid") > -1):
            thisName = line[line.find("uid") +5 : line.find(";") -1]
            
        # hostname
        if(line.find("client-hostname") > -1):
            thisName = line[line.find("hostname") +10 : line.find(";") -1]
            
    #final line
    if (thisIp != ""):
        output[thisIp] = thisIp + " " + thisMAC + " " + thisName

    #print output
    for k, v in sorted(output.items(), key=ip_key):
        print(v)

    # Close the file
    f.close()
    
#parse("/home/james/Source/LeaseInfo/dhcpd.leases")
parse("dhcpd.leases")

# <codecell>


