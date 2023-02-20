Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/jammy64"
    config.vm.hostname = "jackkiwema.com"
    config.vm.network "forwarded_port", adapter: 2, guest: 80, host: 8080, host_ip: "0.0.0.0"
    config.vm.network "public_network", adapter: 2, ip: "192.168.0.50", bridge: "enp0s25", hostname: true
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  
    config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update -y
      sudo apt-get -y install python3 python3-venv python3-dev
      sudo apt-get -y install mysql-server supervisor nginx git
    SHELL
  end
  