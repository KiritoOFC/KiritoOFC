sudo apt install -y golang ffmpeg git build-essential cmake pkg-config libssl-dev python3 python3-pip

cd /media/sf_Downloads/YukkiMusic || cd ~/YukkiMusic
mkdir -p _ntgcalls_tmp
cd _ntgcalls_tmp
wget https://files.pythonhosted.org/packages/source/n/ntgcalls/ntgcalls-1.3.4.tar.gz
tar -xzf ntgcalls-1.3.4.tar.gz
cp ntgcalls-1.3.4/ntgcalls/ntgcalls.h ../ntgcalls/
cd ntgcalls-1.3.4
python3 setup.py build_lib --shared
find shared-output -name "libntgcalls.so"
