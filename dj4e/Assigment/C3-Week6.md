<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DJ4E - Django for Everybody</title>
        <script>
        var _TSUGI = {
            ajax_session: false,
            heartbeat: 1500000,
            heartbeat_url: "https://www.dj4e.com/tsugi/util/heartbeat?msec=1500000",
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_load.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_load.md","full":"\/assn\/dj4e_load.md"},
            spinnerUrl: "https://static.tsugi.org/img/spinner.gif",
            staticroot: "https://static.tsugi.org",
            websocket_url: false,
            websocket_token: false,
            window_close_message: "Application complete",
            session_expire_message: "Your session has expired"
        }
        </script>
        <!-- Tiny bit of JS -->
        <script src="https://static.tsugi.org/js/tsugiscripts_head.js"></script>
        <!-- Le styles -->
        <link href="https://static.tsugi.org/bootstrap-3.4.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.css" rel="stylesheet">
                <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/all.css" rel="stylesheet">
        <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/v4-shims.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Roboto:400" rel="stylesheet"><style>:root {--primary:#0a4b33;--primary-menu:#0a4b33;--primary-border:#0a4630;--primary-darker:#09442e;--primary-darkest:#093e2b;--secondary:#EEEEEE;--secondary-menu:#EEEEEE;--text:#111111;--text-light:#5E5E5E;#FFFFFF;--font-family:'Roboto', Corbel, Avenir, 'Lucida Grande', 'Lucida Sans', sans-serif;--font-size:14px;}</style>
          <link href="https://static.tsugi.org/css/tsugi2.css" rel="stylesheet">

          <style>
                        </style>
<style>
a[target="_blank"]:after {
    font-family: 'Font Awesome 5 Free';
    font-weight: 600;
    content: " \f35d";
}
.goog-te-banner-frame.skiptranslate {
    display: none !important;
    }
body {
    top: 0px !important;
    }
</style>

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/html5shiv/html5shiv.js"></script>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/respond/respond.min.js"></script>
        <![endif]-->

    <script type="text/javascript">CSRF_TOKEN = "TODORemoveThis";</script>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation" id="tsugi_main_nav_bar" style="display:none">  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="https://www.dj4e.com">DJ4E</a>
    </div>
    <div class="navbar-collapse collapse">
      <ul class="nav navbar-nav navbar-main">
        <li><a href="https://www.dj4e.com/lessons" >Lessons</a></li>
        <li><a href="https://www.dj4e.com/assn" >Assignments</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="http://www.dr-chuck.com" target="_blank" >Instructor</a></li>
        <li><a href="https://www.dj4e.com/tsugi/login.php" >Login</a></li>
      </ul>
    </div> <!--/.nav-collapse -->
  </div> <!--container -->
</nav>
<script>
if ( ! inIframe() ) {
  document.getElementById('tsugi_main_nav_bar').style.display = 'block';
  document.getElementsByTagName('body')[0].style.paddingTop = '5.93rem';
}
</script>
<div id="flashmessages"></div><style>
center {
    padding-bottom: 10px;
}
@media print {
    #chapters {
        display: none;
    }
}
a[target="_blank"]:after {
  content: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==);
  margin: 0 3px 0 5px;
}
</style>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<script>
function onSelect() {
    console.log($('#chapters').val());
    window.location = $('#chapters').val();
}
</script>
<div style="float:right">
<select id="chapters" onchange="onSelect();">
  <option value="dj4e_install.md">Django and PythonAnywhere</option>
  <option value="dj4e_html.md">Adding HTML</option>
  <option value="dj4e_tut01.md">Serving Dynamic Content</option>
  <option value="dj4e_tut02.md">Django Models</option>
  <option value="dj4e_tut03.md">Django Views</option>
  <option value="dj4e_tut04.md">Django Forms</option>
  <option value="dj4e_hello.md">Hello Session World</option>
  <option value="dj4e_load.md" selected>Batch Loading Data</option>
  <option value="dj4e_autos.md">Login / Autos CRUD</option>
  <option value="dj4e_local.md">Installing Django Locally</option>
  <option value="dj4e_github.md">Using GitHub</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Building and Loading a Data Model</h1>
<p>In this assignment you will temporarily step away from building the LocalLibrary applications and
develop a data model from a file of un-normalized data and
then build a script to load data in to that model.</p>
<p>The data is a simplified extraction
of the <a href="https://whc.unesco.org/en/list/" tatget="_blank">UNESCO World Heritage Sites</a> registry.
The un-normalized data is provided as both a spreadsheet and a CSF file:</p>
<p><a href="dj4e_load/whc-sites-2018-clean.csv" target="_blank">CSV Version</a></p>
<p><a href="dj4e_load/whc-sites-2018-small.xls" target="_blank">XLS Version</a></p>
<p>The columns in the data are as follows:</p>
<pre><code>name,description,justification,year,longitude,latitude,
area_hectares,category,states,region,iso</code></pre>
<h2>Getting Started</h2>
<p>We will do this assignment within your library application but it will not have any user
interface other than using the admin interface to verify that your application is working.</p>
<p>Make new application under your <code>django_projects/mysite</code> called <code>unesco</code>.</p>
<pre><code>cd ~/django_projects/mysite
python3 manage.py startapp unesco</code></pre>
<p>Also make a folder called <code>scripts</code> and add an <code>__init__.py</code> file to it.  The <code>__init__.py</code> file
is needed in order to store Python objects in the <code>scripts</code> folder.</p>
<pre><code>cd ~/django_projects/mysite
mkdir scripts
touch scripts/__init__.py</code></pre>
<p>Make a copy of the <code>many_load.py</code> from this folder into your <code>scripts</code> folder:</p>
<p><a href="https://github.com/csev/dj4e-samples/tree/master/scripts">https://github.com/csev/dj4e-samples/tree/master/scripts</a></p>
<p>install <code>django extensions</code>:</p>
<pre><code>workon django3                     # If necessary
pip3 install django_extensions</code></pre>
<p>Add the following line to your <code>mysite/mysite/settings.py</code>:</p>
<pre><code>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
...
    'django_extensions', # Add
    'unesco.apps.UnescoConfig',  # Add
]</code></pre>
<h2>Design a Data Model</h2>
<p>You are to design a database model that represents this flat data across
multiple tables using &quot;third-normal form&quot; - which basically means that
columns that have vertical duplication, such as region:</p>
<pre><code>category    states                 region                      iso

Cultural    Afghanistan            Asia and the Pacific        af
Cultural    Afghanistan            Asia and the Pacific        af
Cultural    Albania                Europe and North America    al
Cultural    Albania                Europe and North America    al
Cultural    Algeria                Arab States                 dz
Mixed       Algeria                Arab States                 dz
Cultural    Algeria                Arab States                 dz
Cultural    Algeria                Arab States                 dz</code></pre>
<p>You will make a Django model that describes the tables, one-to-many relationships,
and foreign keys sufficient to represent this data efficiently with no vertical duplication.
Numbers and dates do not have to have their own tables.</p>
<p>Name the first model <code>Site</code>, use singular names for all of the table/model
names.  Use the exact name of the column for the model field names and
foreign key names.  Here is a subset of the <code>unesco/models.py</code>:</p>
<pre><code>from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

...

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    ....

    def __str__(self) :
        return self.name</code></pre>
<p>All of the columns from the CSV data must be represented somewhere in the
data model.  There should be five models in your design, and four One-To-Many
relationships and no Many-to-Many relationships.</p>
<p>Also add the models to <code>unesco/admin.py</code> so you can view them in the administrator interface:</p>
<pre><code>from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, ...

admin.site.register(Site)
admin.site.register(Category)
...</code></pre>
<p>Once you have your model built, run <code>makemigrations</code> and <code>migrate</code> to create
the database.</p>
<pre><code>cd ~/django_projects/mysite
python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
<p>You can repeat the process of editing the <code>models.py</code> file and re-running the migrations steps
until you get them right.</p>
<h2>Loading Data Into Your Database</h2>
<p>Django has a special <code>runscript</code> capability that allows you to write a a Python program
to read and write the database using your Django models.</p>
<p>There is a simple example of how to write such a script in the
<code>dj4e-samples</code> respoistory:</p>
<p><a href="https://github.com/csev/dj4e-samples/blob/master/many/models.py" target="_blank">Many-to-Many / Data Model</a></p>
<p><a href="https://github.com/csev/dj4e-samples/blob/master/scripts/many_load.py" target="_blank">Many-to-Many / Script</a></p>
<p>See the file <code>load.csv</code> and <code>many_load.py</code> for and example of how you look through a file,
insert model data and make foreign key connections.  A key technique is in this bit of code:</p>
<pre><code>p, created = Person.objects.get_or_create(email=row[0])</code></pre>
<p>This code insures that there is a row in the Person table for the email address
that was just read <code>row[0]</code>.  The email address may or may not already be in the table
from a previous line in the file. One way or another, by the end of this line
of code <code>p</code> contains a reference to a Person stored in the database that can be
used to fullfill a foreign key later in the code.</p>
<p>Note that the &quot;p, created&quot; is an example of Python function
<a href="https://youtu.be/CaVhM65wD6g?t=254" target="_blank">returning two values</a>
using a tuple.</p>
<pre><code>m = Membership(role=r,person=p, course=c)
m.save()</code></pre>
<p>The line to make the <code>Membership</code> row is the last thing that is done so all the
foreign key connections can be made.</p>
<p>Notice that the code empties the three tables out every time and freshly reloads
all the data so the process can be run over and over.</p>
<h2>Dealing with Empty Columns</h2>
<p>Your data will be more complex than the sample, You will need to deal with situations
where an integer column like the <code>year</code> will be empty.  First, add <code>null=True</code> to numeric columns
that can be empty in your <code>models.py</code>.   Then before inserting the <code>Site</code> record, check the year to
see if it is a valid integer and if it is not a valid integer set it to <code>None</code> which will become
<code>NULL</code> (or empty) in the data base when inserted:</p>
<pre><code>try:
    y = int(row[3])
except:
    y = None

...

site = Site(name=row[0], description=row[1], year=y, ... )
site.save()</code></pre>
<p>You will need to do this for each of the numeric fields that might be missing.</p>
<h2>Running the Script</h2>
<p>Place the CSV file in the <code>unesco</code> folder and then run the script from the project folder (i.e.
where the <code>manage.py</code> file resides):</p>
<pre><code>cd ~/django_projects/library
workon django3                             # if necessary
python3 manage.py runscript many_load</code></pre>
<p>It needs to be run this way so that lines like:</p>
<pre><code>from unesco.models import Site, Iso, ....</code></pre>
<p>work properly.</p>
<h2>Checking Your Data By Hand</h2>
<p>You can check to see if your data was loaded properly in the Django
Admin user interface.</p>
<p>You can also hand-check your data by running a few queries on
your data before turning it in to make sure the data makes
it into the right tables:</p>
<pre><code>$ sqlite3 db.sqlite3
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite&gt; SELECT count(id) FROM unesco_states;
163
sqlite&gt; SELECT count(id) FROM unesco_site;
1044
sqlite&gt; SELECT count(id) FROM unesco_states where name="India";
1
sqlite&gt; SELECT count(id) FROM unesco_site WHERE name="Hawaii Volcanoes National Park" AND year=1987 AND area_hectares = 87940.0;
1
sqlite&gt; SELECT COUNT(*) FROM unesco_site JOIN unesco_iso ON iso_id=unesco_iso.id WHERE unesco_site.name="Maritime Greenwich" AND unesco_iso.name = "gb";
1
sqlite&gt;</code></pre>
<h2>Once This Assignment is Done</h2>
<p>We added this project to <code>mysite</code> and added the models to the admin user interface so
you could look at them, but you might not want to see the <code>unesco</code> data from this point forward.
Simply comment out the line in <code>mysite/mysite/settings.py</code> as follows:</p>
<pre><code>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
...
    'django_extensions',
    # 'unesco.apps.UnescoConfig',  # Comment out
]</code></pre>
<p>And then restart your web application and verify that the unesco tables no longer show up in the
administrator interface.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
<script src="https://static.tsugi.org/bootstrap-3.4.1/js/bootstrap.min.js"></script>
<script src="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.js"></script>
<script src="https://static.tsugi.org/js/jquery.timeago-1.6.3.js"></script>
<script src="https://static.tsugi.org/js/handlebars-v4.0.2.js"></script>
<script src="https://static.tsugi.org/tmpljs-3.8.0/tmpl.min.js"></script>
<script src="https://static.tsugi.org/js/tsugiscripts.js"></script>
<script type="text/javascript">
    HEARTBEAT_TIMEOUT = setTimeout(doHeartBeat, _TSUGI.heartbeat);
    tsugiEmbedMenu();
</script>
<div id="google_translate_element" style="position: fixed; right: 1em; bottom: 0.25em;"></div><script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: "en", layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, "google_translate_element");
}
</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

<p style="font-size: 75%; margin-top: 5em;">
Copyright Creative Commons Attribution 3.0
</p><script>
// https://stackoverflow.com/questions/7901679/jquery-add-target-blank-for-outgoing-link
$(window).load(function() {
    $('a[href^="http"]').attr('target', function() {
      if(this.host == location.host) return '_self'
      else return '_blank'
    });
});
</script>

</div></body>
</html>
