# Woodog 🐶

Woodog is an initiative to provide help to increasing stray animals by providing them food and refuge by connecting them with fellow helpful humans.
On the application, two types of people can be registered: one who can provide the location and condition of a nearby stray, and another who can provide information and arrange shelter and food for them.

Django and bootstrap are incorporated into the application, requiring authentication and establishing profiles and positioning using maps.

## Instructions to setup 📘

<details>
<summary>
Step 1: Downloading and Installing the Code Editor
</summary>
<br>
You can download and install any one of the following code editors.
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
Step 10: Download and Install postgreSQL(DataBase)
</summary>
<br>

* Download <a href="https://www.postgresql.org/download/">postgreSQL</a>
* Install it.
* Add postgreSQL to path.
</details>

---

<details>
<summary>
Step 11: Create Database named 'woodog'
</summary>
<br>

To create database in postgreSQL,

```bash
createdb --username=postgres woodog
```
</details>

---

<details>
<summary>
Step 12: Making database migrations
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
Step 13: Creating superuser to access Admin Panel
</summary>
<br>

```bash
python manage.py createsuperuser
```
</details>

---

<details>
<summary>
Step 14: Running the Project in local server
</summary>
<br>
<b>Note:</b> Before running the project in local server, Make sure you activate the Virtual Environment.
<br><br>

```bash
python manage.py runserver
http://www.localhost:3000
```
</details>

---

## :bulb: Pro Tip!

* Always keep updating your master branch with the main repository by running the following command on the local master branch. Refer <a href="https://stackoverflow.com/questions/7244321/how-do-i-update-or-sync-a-forked-repository-on-github#:~:text=git%20remote%20add%20upstream%20https://github.com/whoever/whatever.git">this stackoverflow page.</a>

```bash
git pull upstream master
```

* Always create a new branch before making any changes. Never ever make any changes directly on the master branch. To create a **new** branch,

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

---
<p align="center">
<a href="https://github.com/Feminine-Divine/Woodog" title="Woodog Github">
<img src="https://user-images.githubusercontent.com/58631762/120077716-60cded80-c0c9-11eb-983d-80dfa5862d8a.png" width="19">
</a>
</p>