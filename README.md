# NetzclubChecker
Account checker for netzclub.net accounts.
Displays current used traffic and traffic available without the need to install an app or use the official website.

### Installation
1. Install Python using [this tutorial](https://gist.github.com/farOverNinethousand/2efc03be38c9932a338f1336fbef7977#python-installieren-windows)
2. Install the following pip modules using [this tutorial](https://gist.github.com/farOverNinethousand/2efc03be38c9932a338f1336fbef7977#python-module-installieren-windows):  
`` requests ``
3. Download and unzip this project.

### Usage
Run Checker.py and follow displayed instructions.
You do not necessarily have to enter your [netzclub.net](https://www.netzclub.net/login/) password but it is recommended. 
On the first run you will receive a confirmation SMS.
Be sure to run this script 2-3 times every day to make sure your account stays active.  
If everything works as expected, you should get an output like this:
```
***************************************************************************
[netzclub] Traffic left: 299MB/300MB
[netzclub+] Your extra traffic now: 0MB
[netzclub+] You will get 300MB extra traffic in 6 days
[netzclub+] Last time extra traffic: 01-10-2019 02:00:09
[netzclub+] Last time active: 01-02-2020 13:55:48
***************************************************************************
```

### FAQ
**Can I use this script and the [netzclub+ app](https://play.google.com/store/apps/details?id=net.netzclub.plus) at the same time?**  
No. If you use this script you will be automatically logged out in the netzclub+ app and the other way around.
You will then have to re-enter that confirmation SMS.

**Can I use this script and the [normal netzclub app](https://play.google.com/store/apps/details?id=com.telefonica.netzclub.csc) at the same time?**  
Yes.

**Will my account get banned if I use this script?**  
No gurantees but I don't see any reason why this should happen at this moment.

**Can I use this script with multiple netzclub accounts?**  
Not in a comfortable way but you can copy it multiple times and add different accounts for each copy ;)