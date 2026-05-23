# Software and Hardware Requirements

This document captures the reference Linux workstation and the practical requirements for building and running `motorweb`.

---

## 1. Minimum Requirements

For the current FastAPI Job Application Platform:

```text
Linux workstation
Python 3.13
python3.13-venv
Git
OpenSSH client
curl
zip/unzip
```

Recommended hardware:

```text
4+ CPU cores
8+ GiB RAM
20+ GiB free disk
```

Better for Docker/Kubernetes later:

```text
8+ CPU cores
16+ GiB RAM
100+ GiB free disk
```

---

## 2. Reference Machine Summary

Captured reference machine:

```text
OS: Pop!_OS 22.04 LTS
Kernel: 6.17.9-76061709-generic
CPU: AMD Ryzen 9 8945HS w/ Radeon 780M Graphics
CPU cores/threads: 8 cores / 16 logical CPUs
Memory: 60 GiB RAM
Swap: 15 GiB
Root filesystem: 934 GiB total, 763 GiB available at capture time
Disk: NVMe, encrypted LUKS + LVM, ext4 root filesystem
```

This is more than enough for:

```text
FastAPI development
Docker
local Kubernetes experiments
Prometheus/Grafana
homelab preparation
```

---

## 3. Reference Software Summary

Captured development tools:

```text
Python default: 3.10.12
Python project version: 3.13.13
Git: 2.34.1
OpenSSH: 8.9p1
curl: 7.81.0
zip: 3.0
unzip: 6.00
Docker: 29.1.4-rd
kubectl: 1.33.3
Helm: 4.0.5
Java: 25 LTS
Node.js: 22.20.0
npm: 11.9.0
PyCharm: 2026.1
Obsidian: installed
Insomnia: installed
Postman: not installed
kind: not installed
```

---

## 4. Important Python Note

Captured output showed:

```text
pip command not found
```

That is okay for this project if using venv correctly.

Preferred workflow:

```bash
cd /opt/projects/motorweb/apps/job-application-platform
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Inside the virtual environment:

```bash
python --version
python -m pip --version
```

should work.

If venv creation fails, install:

```bash
sudo apt update
sudo apt install python3.13-venv
```

---

## 5. Raw Captured Machine Output

```text
#!/bin/bash

pl@pop-os:/opt/projects/motorweb$ echo "=== OS ==="
cat /etc/os-release

echo
echo "=== Kernel ==="
uname -a

echo
echo "=== CPU ==="
lscpu

echo
echo "=== Memory ==="
free -h

echo
echo "=== Disk ==="
df -h /

echo
echo "=== Block Devices ==="
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
=== OS ===
NAME="Pop!_OS"
VERSION="22.04 LTS"
ID=pop
ID_LIKE="ubuntu debian"
PRETTY_NAME="Pop!_OS 22.04 LTS"
VERSION_ID="22.04"
HOME_URL="https://pop.system76.com"
SUPPORT_URL="https://support.system76.com"
BUG_REPORT_URL="https://github.com/pop-os/pop/issues"
PRIVACY_POLICY_URL="https://system76.com/privacy"
VERSION_CODENAME=jammy
UBUNTU_CODENAME=jammy
LOGO=distributor-logo-pop-os

=== Kernel ===
Linux pop-os 6.17.9-76061709-generic #202511241048~1778249354~22.04~d91a106 SMP PREEMPT_DYNAMIC Fri M x86_64 x86_64 x86_64 GNU/Linux

=== CPU ===
Architecture:                x86_64
  CPU op-mode(s):            32-bit, 64-bit
  Address sizes:             48 bits physical, 48 bits virtual
  Byte Order:                Little Endian
CPU(s):                      16
  On-line CPU(s) list:       0-15
Vendor ID:                   AuthenticAMD
  Model name:                AMD Ryzen 9 8945HS w/ Radeon 780M Graphics
    CPU family:              25
    Model:                   117
    Thread(s) per core:      2
    Core(s) per socket:      8
    Socket(s):               1
    Stepping:                2
    Frequency boost:         enabled
    CPU max MHz:             5263.0610
    CPU min MHz:             402.7860
    BogoMIPS:                7985.38
    Flags:                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clfl
                             ush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm consta
                             nt_tsc rep_good amd_lbr_v2 nopl xtopology nonstop_tsc cpuid extd_apicid aper
                             fmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe 
                             popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy a
                             bm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_c
                             ore perfctr_nb bpext perfctr_llc mwaitx cpuid_fault cpb cat_l3 cdp_l3 hw_pst
                             ate ssbd mba perfmon_v2 ibrs ibpb stibp ibrs_enhanced vmmcall fsgsbase bmi1 
                             avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx51
                             2ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xget
                             bv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx5
                             12_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock 
                             nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthres
                             hold vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfn
                             i vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid overflow_
                             recov succor smca fsrm flush_l1d
Virtualization features:     
  Virtualization:            AMD-V
Caches (sum of all):         
  L1d:                       256 KiB (8 instances)
  L1i:                       256 KiB (8 instances)
  L2:                        8 MiB (8 instances)
  L3:                        16 MiB (1 instance)
NUMA:                        
  NUMA node(s):              1
  NUMA node0 CPU(s):         0-15
Vulnerabilities:             
  Gather data sampling:      Not affected
  Ghostwrite:                Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Old microcode:             Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Mitigation; Safe RET
  Spec store bypass:         Mitigation; Speculative Store Bypass disabled via prctl
  Spectre v1:                Mitigation; usercopy/swapgs barriers and __user pointer sanitization
  Spectre v2:                Mitigation; Enhanced / Automatic IBRS; IBPB conditional; STIBP always-on; PB
                             RSB-eIBRS Not affected; BHI Not affected
  Srbds:                     Not affected
  Tsa:                       Vulnerable: No microcode
  Tsx async abort:           Not affected
  Vmscape:                   Mitigation; IBPB before exit to userspace

=== Memory ===
               total        used        free      shared  buff/cache   available
Mem:            60Gi       8.4Gi        47Gi       146Mi       4.7Gi        48Gi
Swap:           15Gi          0B        15Gi

=== Disk ===
Filesystem             Size  Used Avail Use% Mounted on
/dev/mapper/data-root  934G  123G  763G  14% /

=== Block Devices ===
NAME              SIZE TYPE  FSTYPE      MOUNTPOINTS
zram0              16G disk              [SWAP]
nvme0n1         953.9G disk              
├─nvme0n1p1       976M part  vfat        /boot/efi
├─nvme0n1p2       3.8G part  vfat        /recovery
└─nvme0n1p3     949.1G part  crypto_LUKS 
  └─cryptdata   949.1G crypt LVM2_member 
    └─data-root 949.1G lvm   ext4        /
pl@pop-os:/opt/projects/motorweb$ 

```

---

## 6. Raw Captured Python/Git/Dev Tools Output

```text
echo "=== Python ==="
python3 --version
python3.13 --version
pip --version

echo
echo "=== Git ==="
git --version

echo
echo "=== SSH ==="
ssh -V

echo
echo "=== curl ==="
curl --version | head -5

echo
echo "=== unzip/zip ==="
zip --version | head -2
unzip -v | head -2


pl@pop-os:/opt/projects/motorweb$ echo "=== Python ==="
python3 --version
python3.13 --version
pip --version

echo
echo "=== Git ==="
git --version

echo
echo "=== SSH ==="
ssh -V

echo
echo "=== curl ==="
curl --version | head -5

echo
echo "=== unzip/zip ==="
zip --version | head -2
unzip -v | head -2
=== Python ===
Python 3.10.12
Python 3.13.13
Command 'pip' not found, but can be installed with:
sudo apt install python3-pip

=== Git ===
git version 2.34.1

=== SSH ===
OpenSSH_8.9p1 Ubuntu-3ubuntu0.15, OpenSSL 3.0.2 15 Mar 2022

=== curl ===
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.20
Release-Date: 2022-01-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp 
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd

=== unzip/zip ===
Copyright (c) 1990-2008 Info-ZIP - Type 'zip "-L"' for software license.
This is Zip 3.0 (July 5th 2008), by Info-ZIP.
UnZip 6.00 of 20 April 2009, by Debian. Original by Info-ZIP.

pl@pop-os:/opt/projects/motorweb$ 


```

---

## 7. Raw Captured Optional Tools Output

```text
pl@pop-os:/opt/projects/motorweb$ echo "=== Docker ==="
docker --version 2>/dev/null || echo "docker not installed"

echo
echo "=== kubectl ==="
kubectl version --client 2>/dev/null || echo "kubectl not installed"

echo
echo "=== kind ==="
kind --version 2>/dev/null || echo "kind not installed"

echo
echo "=== helm ==="
helm version 2>/dev/null || echo "helm not installed"

echo
echo "=== Java ==="
java -version 2>&1 | head -3

echo
echo "=== Node / npm ==="
node --version 2>/dev/null || echo "node not installed"
npm --version 2>/dev/null || echo "npm not installed"
=== Docker ===
Docker version 29.1.4-rd, build 3c6914c

=== kubectl ===
Client Version: v1.33.3
Kustomize Version: v5.6.0

=== kind ===
kind not installed

=== helm ===
version.BuildInfo{Version:"v4.0.5", GitCommit:"1b6053d48b51673c5581973f5ae7e104f627fcf5", GitTreeState:"clean", GoVersion:"go1.25.5", KubeClientVersion:"v1.34"}

=== Java ===
java version "25" 2025-09-16 LTS
Java(TM) SE Runtime Environment (build 25+37-LTS-3491)
Java HotSpot(TM) 64-Bit Server VM (build 25+37-LTS-3491, mixed mode, sharing)

=== Node / npm ===
v22.20.0
11.9.0
pl@pop-os:/opt/projects/motorweb$ 


```

---

## 8. Raw Captured Desktop Tools Output

```text
echo "=== JetBrains / PyCharm candidates ==="
ls -d /opt/pycharm* 2>/dev/null || true
ls -d ~/.local/share/JetBrains/* 2>/dev/null || true

echo
echo "=== Obsidian ==="
which obsidian 2>/dev/null || echo "obsidian command not found"
ls -d /opt/Obsidian 2>/dev/null || true

echo
echo "=== API clients ==="
which postman 2>/dev/null || echo "postman command not found"
which insomnia 2>/dev/null || echo "insomnia command not found"
ls -d /opt/Insomnia 2>/dev/null || true

pl@pop-os:/opt/projects/motorweb$ echo "=== JetBrains / PyCharm candidates ==="
ls -d /opt/pycharm* 2>/dev/null || true
ls -d ~/.local/share/JetBrains/* 2>/dev/null || true

echo
echo "=== Obsidian ==="
which obsidian 2>/dev/null || echo "obsidian command not found"
ls -d /opt/Obsidian 2>/dev/null || true

echo
echo "=== API clients ==="
which postman 2>/dev/null || echo "postman command not found"
which insomnia 2>/dev/null || echo "insomnia command not found"
ls -d /opt/Insomnia 2>/dev/null || true
=== JetBrains / PyCharm candidates ===
/home/pl/.local/share/JetBrains/bl              /home/pl/.local/share/JetBrains/IntelliJIdea2025.2
/home/pl/.local/share/JetBrains/consentOptions  /home/pl/.local/share/JetBrains/IntelliJIdea2026.1
/home/pl/.local/share/JetBrains/crl             /home/pl/.local/share/JetBrains/PyCharm2026.1
/home/pl/.local/share/JetBrains/Daemon          /home/pl/.local/share/JetBrains/Toolbox

=== Obsidian ===
/home/pl/.local/bin/obsidian
/opt/Obsidian

=== API clients ===
postman command not found
/usr/bin/insomnia
/opt/Insomnia
pl@pop-os:/opt/projects/motorweb$ 


```
