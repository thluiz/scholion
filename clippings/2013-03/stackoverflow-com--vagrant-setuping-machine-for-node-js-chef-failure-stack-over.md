---
url: "http://stackoverflow.com/questions/13549020/vagrant-setuping-machine-for-node-js-chef-failure"
captured_at: "2013-03-16T14:10:21-03:00"
title: "Vagrant, setuping machine for Node.js - Chef failure - Stack Overflow"
domain: "stackoverflow-com"
---

# **V**agrant, setuping machine for Node.js

My Vargrant file,

```
Vagrant::Config.run do |config|
  config.vm.box = "lucid32"
  config.ssh.forward_agent = true
  config.vm.forward_port 3000, 3000

  # allow for symlinks in the app folder
  config.vm.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/app", "1"]
  config.vm.customize ["modifyvm", :id, "--memory", 512, "--cpus", 1]

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "cookbooks"

    chef.add_recipe "apt"
    chef.add_recipe "build-essential"
    chef.add_recipe "nodejs-cookbook"
    chef.add_recipe "chef-hosts"
    chef.add_recipe "git"
    chef.json = {
      "nodejs" => {
        "version" => "0.8.12",
        "install_method" => "source",
        "npm" => "1.1.62"
      },
      "host_aliases" => [{
        "name" => "awesomeapp",
        "ip" => "127.0.0.1"
      }]
    }
  end
end
```

But on `vagrant reload` - I got such exception from Chef**.**

```
[2012-11-25T07:58:23+01:00] ERROR: Running exception handlers
[2012-11-25T07:58:23+01:00] ERROR: Exception handlers complete
[2012-11-25T07:58:24+01:00] FATAL: Stacktrace dumped to /tmp/vagrant-chef-1/chef-stacktrace.out
[2012-11-25T07:58:24+01:00] FATAL: Chef::Exceptions::CookbookNotFound: Cookbook nodejs not found. If you're loading nodejs from another cookbook, make
sure you configure the dependency in your metadata
Chef never successfully completed! Any errors should be visible in the
output above. Please fix your recipes so that they properly complete.
```

**SOLVED**: In cookbook folder I renamed `nodejs-cookbook` to `nodejs` and corrected Vagrant file**.**

```
chef.add_recipe "nodejs-cookbook"
```

After I run,

```
vargrant provision
```

Everything were installed fine**!**
