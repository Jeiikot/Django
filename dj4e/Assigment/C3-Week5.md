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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_ads1.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_ads1.md","full":"\/assn\/dj4e_ads1.md"},
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
  <option value="dj4e_load.md">Batch Loading Data</option>
  <option value="dj4e_autos.md">Login / Autos CRUD</option>
  <option value="dj4e_local.md">Installing Django Locally</option>
  <option value="dj4e_github.md">Using GitHub</option>
  <option value="dj4e_ads1.md" selected>AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Building a Classified Ad Web Site</h1>
<p>In this assignment, you will build a web site that is roughly equivalent to</p>
<p><a href="https://chucklist.dj4e.com/m1">https://chucklist.dj4e.com/m1</a></p>
<p>This web site is a classified ad web site.   People can view ads without logging in
and if they log in, they can create their own ads.   It uses a social login
that allows loging using github accounts.</p>
<p>You will build this application by borrowing parts and pieces from the code that runs</p>
<p><a href="https://samples.dj4e.com/">https://samples.dj4e.com/</a></p>
<p>and combining them into a single application.</p>
<p>Make sure to get the latest version of dj4e-samples.  If you have never checked it out
on PythonAnywhere:</p>
<pre><code>cd ~
git clone https://github.com/csev/dj4e-samples</code></pre>
<p>If you have already checked <code>dj4e-samples</code>  on PythonAnywhere do:</p>
<pre><code>workon django3
cd ~/dj4e-samples
git pull
pip install -r requirements.txt</code></pre>
<h2>Pulling In Code From Samples</h2>
<p>In this section, we will break and then fix your <code>settings.py</code> and <code>urls.py</code>.
When this is done, the autos, cats, dogs, etc will stop working unless you
add them back to these two files.  It is OK for these applications to be working.
The autograder will just look at /ads.</p>
<p>(1) Copy the <code>settings.py</code> and <code>urls.py</code> files and the entire
<code>home</code> folder from the <code>dj4e-samples</code> project:</p>
<pre><code>cp ~/dj4e-samples/dj4e-samples/settings.py ~/django_projects/mysite/mysite
cp ~/dj4e-samples/dj4e-samples/urls.py ~/django_projects/mysite/mysite
cp -r ~/dj4e-samples/home/* ~/django_projects/mysite/home</code></pre>
<p>(2) Edit <code>~/dango_projects/mysite/mysite/settings.py</code> and then delete
all the <code>INSTALLED_APPLICATIONS</code> after <code>home</code>.  You also have to search
and replace <code>dj4e-samples</code> with <code>mysite</code> in a few places.  Also set
the name of your application in the <code>settings.py</code> file:</p>
<pre><code># Used for a default title
APP_NAME = 'ChucksList'</code></pre>
<p>This shows up in default page titles and default page navigation.</p>
<p>(5) Edit your <code>django_projects/mysite/mysite/urls.py</code> and
remove all of the <code>path()</code> calls to the sample applications. Make
sure to keep the <code>path()</code> to include the <code>home.urls</code>.  Also keep
the <code>site</code> and <code>favicon</code> rules in your <code>urls.py</code>.</p>
<p>(6) Edit the file <code>django_projects/mysite/home/templates/home/main.html</code> and put
this HTML in the file:</p>
<pre><code>&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;{{ settings.APP_NAME }}&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Welcome to {{ settings.APP_NAME }}&lt;/h1&gt;
    &lt;p&gt;
    Hello world.
    &lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>(7) At this point, you should be able to run:</p>
<pre><code>python3 manage.py check</code></pre>
<p>Keep running <code>check</code> until it does not find any errors.</p>
<p>If you restart your web application, there won't be many working urls.
Try these two to see if you have the home code working properly:</p>
<pre><code>https://your-account.pythonanywhere.com/
https://your-account.pythonanywhere.com/favicon.ico
https://your-account.pythonanywhere.com/accounts/login</code></pre>
<p>Look at how pretty the login form looks :).
Don't worry about social login yet.  We will get to that later.
Favicons are shown in the tabs in the browser.  We will get to favicons later too :)</p>
<p>If you get an error like <code>Could not import github_settings.py for social_django</code>
when running <code>manage.py</code> or restarting your PythonAnywhere webapp,
don't worry - you will see this warning until you set up social login.</p>
<h2>Building the Ads Application</h2>
<p>In this section, you will pull bits and pieces of the sample applications repository and pull them
into your <code>ads</code> application.  </p>
<p><strong>Important Note:</strong> If you find you have a problem saving files in the PythonAnywhere
system using their browser-based editor, you might need to turn off your ad blocker for
this site - weird bt true.</p>
<p>(1) Create a new <code>ads</code> application within your <code>mysite</code> project:</p>
<pre><code>cd django_projects/mysite
python3 manage.py startapp ads</code></pre>
<p>The add the application to your <code>mysite/mysite/settings.py</code> and `mysite/mysite/urls.py'.</p>
<p>(2) Use this in your <code>ads/model.py</code>:</p>
<pre><code>from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title</code></pre>
<p>(3) Copy the <code>owner.py</code> from <code>myarts</code> to your ads application.  This is the one file you <b>do not</b>
have to change at all (thanks to object orientation :) ).</p>
<p>(4) The files <code>admin.py</code>, <code>views.py</code>, <code>urls.py</code>, and the <code>templates</code> folder will require significant
adaptation to be suitable for a classified
ad application and the above model.   A big part of this assignment is to use the
view classes that are in <code>owner.py</code> and used in <code>views.py</code>.  The new <code>owner</code> field should
not be shown to the user on the create and update forms, it should be automatically set
by the classes like <code>OwnerCreateView</code> in <code>owner.py</code>.  If you see an &quot;owner&quot; drop down
in your create screen the program is not implemented correctly and will fail the autograder.</p>
<p>(5) When you are implementing the update and delete views, make sure to follow the url patterns
for the update and delete operations.  They should be of the form <code>/ad/14/update</code>
and <code>/ad/14/delete</code>.  Something like the following should work in your <code>urls.py</code>:</p>
<pre><code>from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view()),
    path('ads', views.AdListView.as_view(), name='all'),
    path('ad/&lt;int:pk&gt;', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('ad/&lt;int:pk&gt;/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('ad/&lt;int:pk&gt;/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
]</code></pre>
<p>(6) Ad you build the application, use <code>check</code> periodically as you complete some of the code.</p>
<pre><code>python3 manage.py check</code></pre>
<p>(7) Once your application is mostly complete and can pass the <code>check</code>
without error, add the new models to your migrations and database tables:</p>
<pre><code>python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
<h2>Debugging: Searching through all your files in the bash shell</h2>
<p>If you have errors, you might find the <code>grep</code> tool very helpful in figuring out where you might find your errors.
For example, lets say after you did all the editing, and went to the ads url and got this error:</p>
<pre><code>NoReverseMatch at /ads
'myarts' is not a registered namespace</code></pre>
<p>You <em>thought</em> you fixed all the instances where the string &quot;myarts&quot; was in your code, but you must have missed one.
You can manually look at every file individually or use the following command to let the computer do the searching:</p>
<pre><code>cd ~/django_projects/mysite
grep -ri myarts *</code></pre>
<p>You might see output like this:</p>
<pre><code>ads/templates/ads/ad_list.html:&lt;a href="{% url 'login' %}?next={% url 'myarts:all' %}"&gt;Login&lt;/a&gt;</code></pre>
<p>The <code>grep</code> program is searching for all the files in the current folder and in subfolders for any lines
in any file that have the string &quot;myarts&quot; in them and shows you the file name and the line within the file.</p>
<p>The <code>grep</code> command is the <a href="https://en.wikipedia.org/wiki/Grep" target="_blank">&quot;Generalized Regular
Expression Parser&quot;</a> and is one of the most useful Linux commands to know.
The 'r' means 'recursive' and the 'i' means 'ignore case.   The <code>grep</code> program will save you so much time :).</p>
<h2>Adding the Bootstrap menu to the top of the page</h2>
<p>Next we will add the bootstrap navigation bar to the top of your application as shown in:</p>
<p><a href="https://chucklist.dj4e.com/">https://chucklist.dj4e.com/</a></p>
<p>This top bar includes a 'Create Ad' navigation item and the login/logout navigation as well as
the gravatar when the user logs in.</p>
<p>(2) Edit all four of the <code>ads_</code> files in <code>ads/templates/ads</code> to change them so
they extend <code>ads/base_menu.html</code>.  Change the first line of each file from:</p>
<pre><code>{% extends "base_bootstrap.html" %}</code></pre>
<p>to be:</p>
<pre><code>{% extends "base_menu.html" %}</code></pre>
<p>(3) Then create <code>home/templates/base_menu.html</code> with the following content:</p>
<pre><code>{% extends "base_bootstrap.html" %}
{% block navbar %}
{% load app_tags %}
&lt;nav class="navbar navbar-default navbar-inverse"&gt;
  &lt;div class="container-fluid"&gt;
    &lt;div class="navbar-header"&gt;
        &lt;a class="navbar-brand" href="/"&gt;{{ settings.APP_NAME }}&lt;/a&gt;
    &lt;/div&gt;
    &lt;!-- https://stackoverflow.com/questions/22047251/django-dynamically-get-view-url-and-check-if-its-the-current-page --&gt;
    &lt;ul class="nav navbar-nav"&gt;
      {% url 'ads' as ads %}
      &lt;li {% if request.get_full_path == ads %}class="active"{% endif %}&gt;
          &lt;a href="{% url 'ads:all' %}"&gt;Ads&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
    &lt;ul class="nav navbar-nav navbar-right"&gt;
        {% if user.is_authenticated %}
        &lt;li&gt;
        &lt;a href="{% url 'ads:ad_create' %}"&gt;Create Ad&lt;/a&gt;
        &lt;/li&gt;
        &lt;li class="dropdown"&gt;
            &lt;a href="#" data-toggle="dropdown" class="dropdown-toggle"&gt;
                &lt;img style="width: 25px;" src="{{ user|gravatar:60 }}"/&gt;&lt;b class="caret"&gt;&lt;/b&gt;
            &lt;/a&gt;
            &lt;ul class="dropdown-menu"&gt;
                &lt;li&gt;&lt;a href="{% url 'logout' %}?next={% url 'ads:all' %}"&gt;Logout&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/li&gt;
        {% else %}
        &lt;li&gt;
        &lt;a href="{% url 'login' %}?next={% url 'ads:all' %}"&gt;Login&lt;/a&gt;
        &lt;/li&gt;
        {% endif %}
    &lt;/ul&gt;
  &lt;/div&gt;
&lt;/nav&gt;
{% endblock %}</code></pre>
<p>(4) Find the line in your <code>base_bootstrap.html</code> that looks like this:</p>
<pre><code>    &lt;meta name="dj4e-code" content="99999999"&gt;</code></pre>
<p>and change the <code>9999999</code>  to be &quot;<span id="dj4e-code">missing</span>&quot;</p>
<p>Make sure to check the autograder for additional markup requirements.</p>
<p>When you are done, you should see an 'Ads' menu on the left and a 'Create Ad' link on the right just like the
sample implementation.</p>
<h2>Fun Challenges</h2>
<p>(1) Make yourself a gravatar at <a href="https://en.gravatar.com/">https://en.gravatar.com/</a> - it is super easy and you will see your
avatar when you log in in your application and elsewhere with gravatar enabled apps. The gravatar can be
anything you like - it does not have to be a picture of you.  The gravatar is associated an email address
so make sure to give an email address to the user you create with <code>createsuperuser</code>.</p>
<p>(2) Change your <code>home/static/favicon.ico</code> to a favicon of your own making.   I made my favicon
at <a href="https://favicon.io/favicon-generator/">https://favicon.io/favicon-generator/</a> - it might not change instantly after you update the favicon
because they are cached extensively.   Probably the best way to test is to go right to the favicon url
after you update the file and press 'Refresh' and/or switch browsers.  Sometimes the browswer caching
is &quot;too effective&quot; on a favicon so to force a real reload to check if the new favicon is really being served
you can add a GET parameter tho the URL to forc it to be re-retrieved:</p>
<pre><code>https://chucklist.dj4e.com/favicon.ico?x=42</code></pre>
<p>Change the <code>x</code> value to something else if you want to test over and over.</p>
<p>(3) Make social login work.  Take a look at
<a href="https://github.com/csev/dj4e-samples/blob/master/dj4e-samples/github_settings-dist.py" target="_blank">
github_settings-dist.py</a>, copy it into
<code>mysite/mysite/github_settings.py</code> and go through the process on github to get your client ID and
secret.   The documentation is in comments of the file.  Also take a look at
<a href="https://github.com/csev/dj4e-samples/blob/master/dj4e-samples/urls.py" target="_blank">
dj4e-samples/urls.py</a> and make sure that the &quot;Switch to social login&quot; code is correct
and at the end of your <code>mysite/mysite/github_settings.py</code>.</p>
<p>You can register two applications with github - one on localhost and one on PythonAnywhere.  If you are
using github login on localhost - make sure that you register <code>http://127.0.0.1:8000/</code> instead
of <code>http://localhost:8000/</code> and use that in your browser to test your site.  If you
use localhost, you probably will get the <code>The redirect_uri MUST match the registered callback URL for this application.</code> error message when you use social login.</p>
<h2>Working with Ambiguity</h2>
<p>This assignment is more vague than previous assignments - on purpose.  The goal is to get
closer to the development model for actual applications.  You know what you want to build
and start with a mostly blank slate.  You look at sample code, reuse some code form stuff
you build earlier, do some online
searching and glue pieces of what you find together to make your application.  Of course as
you are gluing bits from various places together, they always break and you have to adjust things
so they fit in your application.</p>
<p>So this is kind of like the real world - when you have to build your own first application
for someone else.</p>
<p>Let us know if you really get stuck.  We want you to succeed in this assignment.</p>
<script>
var d= new Date();
var code = "42"+((Math.floor(d.getTime()/1234567)*123456)+42)
document.getElementById("dj4e-code").innerHTML = code;
</script><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
