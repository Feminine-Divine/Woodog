<p align = 'center'>
<img src = "https://img.shields.io/badge/Woodog-4285F4?style=%2for-the-badge&logo=datadog&logoColor=white" height = '100' width = '300'/>
</p>
<div align="center">

<a href="https://github.com/Feminine-Divine/Woodog"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>
<a href="https://github.com/Feminine-Divine/Woodog"><img src="https://img.shields.io/badge/Built%20by-developers%20%3C%2F%3E-0059b3"></a>
<a href="https://github.com/Feminine-Divine/Woodog"><img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=yellow"></a>
<a href="https://github.com/Feminine-Divine/"><img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?v=103"></a>
<a href="https://github.com/Feminine-Divine/Woodog"><img src="https://img.shields.io/badge/PR's%3F-Welcomed-brightgreen.svg?v=103"></a>

<a href="https://github.com/Feminine-Divine/Woodog/watchers"><img src="https://img.shields.io/github/watchers/Feminine-Divine/Woodog?style=flat"></a> 
<a href="https://github.com/Feminine-Divine/Woodog/graphs/contributors"><img src="https://img.shields.io/github/contributors/Feminine-Divine/Woodog?color=brightgreen"></a>
<a href="https://github.com/Feminine-Divine/Woodog/stargazers"><img src="https://img.shields.io/github/stars/Feminine-Divine/Woodog?color=0059b3"></a>
<a href="https://github.com/Feminine-Divine/Woodog/network/members"><img src="https://img.shields.io/github/forks/Feminine-Divine/Woodog?color=yellow"></a>
<a href="https://github.com/Feminine-Divine/Woodog/issues"><img src="https://img.shields.io/github/issues/Feminine-Divine/Woodog?color=0059b3"></a>
<a href="https://github.com/Feminine-Divine/Woodog/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed-raw/Feminine-Divine/Woodog?color=yellow"></a>
<a href="https://github.com/Feminine-Divine/Woodog/pulls"><img src="https://img.shields.io/github/issues-pr/Feminine-Divine/Woodog?color=brightgreen"></a>
<a href="https://github.com/Feminine-Divine/Woodog/pulls?q=is%3Apr+is%3Aclosed"><img src="https://img.shields.io/github/issues-pr-closed-raw/Feminine-Divine/Woodog?color=0059b3"></a> 
</div>

Woodog:dog: is an initiative to provide help to increasing stray animals by providing them food :bread: and refuge :house: by connecting them with fellow helpful humans.
On the application, two types of people can be registered :inbox_tray: one who can provide the location and condition of a nearby stray, and another who can provide information and arrange shelter :house: and food :bread: for them.

Django and bootstrap are incorporated into the application, requiring authentication and establishing profiles and positioning using maps.

## Instructions to setup :arrow_down::computer:

<details>
<summary>
Step 1: Downloading and Installing the Code Editor
</summary>
<br>
You can download and install any one of the following IDE.
<br><br>
<ul>
<li><a href="https://code.visualstudio.com/">Visual Studio Code</a> (Preferred)</li>
<li><a href="https://www.sublimetext.com/3">Sublime Text 3</a></li>
<li><a href="https://atom.io/">Atom</a></li>
</details>

---

<details>
<summary>
Step 2: Installing Python
</summary>
<br>
Download <a href="https://www.python.org/downloads/">Python Latest Version</a>
<br><br>
<ul>
<li>Make sure to check '<b>Add Python to Path</b>' in the setup window of the Installer.</li>
</ul>

Verify the installation from the Terminal using the following command,

```bash
python --version
```

</details>

---

<details>
<summary>
Step 3: Installing Git
</summary>
<br>
Download <a href="https://git-scm.com/downloads">Git</a>
</details>

---

<details>
<summary>
Step 4: Fork the Repository
</summary>
<br>
Click on <a href="#" target="_self"><img src="https://user-images.githubusercontent.com/58631762/120588030-11cee200-c454-11eb-98ad-060ef99428c5.png" width="16"></img></a> to fork <a href="https://github.com/Feminine-Divine/Woodog">this</a> repsository
</details>

---

<details>
<summary>
Step 5: Cloning Repository using Git
</summary>
<br>

```bash
git clone https://github.com/'<your-github-username>'/Woodog.git
```
</details>

---

<details>
<summary>
Step 6: Change directory to Woodog
</summary>
<br>

```bash
cd Woodog
```
</details>

---

<details>
<summary>
Step 7: Add reference to the original repository
</summary>
<br>

```bash
git remote add upstream https://github.com/Feminine-Divine/Woodog.git
```
</details>

---

<details>
<summary>
Step 8: Creating Virtual Environment
</summary>
<br>
Install virtualenv
<br><br>

```bash
pip install virtualenv
```

Creating Virtual Environment named `env`

```bash
virtualenv env
```

To Activate `env`

```bash
source env/Scripts/activate
or
./env/Scripts/activate
```

To deactivate `env`

```bash
deactivate
```
</details>

---

<details>
<summary>
Step 9: Installing Requirements
</summary>
<br>

**Note**: Before installing requirements, Make sure the virtual environment is activated.
<br><br>

```bash
cd Woodog
pip install -r requirements.txt
```
</details>

---

<details>
<summary>
Step 10: Making database migrations
</summary>
<br>

**Note**: Before making database migrations, make sure you've successfully created database.

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
</details>

---

<details>
<summary>
Step 11: Creating superuser to access Admin Panel
</summary>
<br>

```bash
python manage.py createsuperuser
```
</details>

---

<details>
<summary>
Step 12: Running the Project in local server
</summary>
<br>
<b>Note:</b> Before running the project in local server, Make sure you activate the Virtual Environment.
<br><br>

```bash
python manage.py runserver
```
<p>Server will be up and running in local host on PORT 8000</p>
</details>

---

## :bulb: Pro Tip!

:one: Always keep updating your master branch with the main repository by running the following command on the local master branch. Refer <a href="https://stackoverflow.com/questions/7244321/how-do-i-update-or-sync-a-forked-repository-on-github#:~:text=git%20remote%20add%20upstream%20https://github.com/whoever/whatever.git">this stackoverflow page.</a>

```bash
git pull upstream master
```

:two: Always create a new branch before making any changes. Never ever make any changes directly on the master branch. To create a **new** branch,

```bash
git checkout -b '<new-branch-name>'
```
---

## Code of conduct ©️

* Please take a moment to review the [Code of Conduct](https://github.com/Feminine-Divine/Woodog/blob/master/CODE_OF_CONDUCT.md) and [contributing.md](https://github.com/Feminine-Divine/Woodog/blob/master/contributing.md) which provides the guidelines for contributing.
---

## Contributing 👷

* <a href="#" target="_self" title="Fork">Fork</a> the project.
* Create your Feature Branch
```bash
git checkout -b '<your_branch_name>'
```
* Stage your changes
```bash
git add .
```
* Commit your changes
```bash
git commit -m '<your_commit_message>'
```
* Check for Status to be sure everything is added
```bash
git status
```
* Check for your remote
```bash
git remote -v
```
* Push changes to remote
```bash
git push origin '<your_branch_name>'
```
* Open a <a href="https://github.com/Feminine-Divine/Woodog/pulls" title="Create Pull request">Pull Request</a>

## 📌 Opensource Programs

### This project is a part of following Open Source Program
<br>

<table style="width:80%;background-color:white;border-radius:30px;">
    <tr>
  <td>
<center>
  <a href="https://letsgrowmore.in/projects/"><img src="https://letsgrowmore.in/wp-content/uploads/2021/05/cropped-growmore-removebg-preview.png"></img></a>
  </center>
  </td>
  </tr>
</table>
    <hr>

  ## Our Project Admins 🤓 

<br>
<table>
<tr>
<td align="center"><a href="https://github.com/Aaishpra"><img src="https://avatars.githubusercontent.com/u/66299533?v=4" width=150px height=150px /></a></br> <h4 style="color:white;">Shipra Verma</h4>

  



<td align="center" ><a href="https://github.com/khushishikhu"><img src="https://avatars.githubusercontent.com/u/65439761?v=4" width=150px height=150px /></a></br> <h4 style="color:white;">Khushi Gautam</h4>

</tr>
</table>
<br>

---


 ## Our Valuable Contributors :


<a href="https://github.com/Feminine-Divine/Woodog/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Feminine-Divine/Woodog" />
</a>

---

<p align="center">
<a href="https://github.com/Feminine-Divine/Woodog" title="Woodog Github">
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
    
</a>
</p>
