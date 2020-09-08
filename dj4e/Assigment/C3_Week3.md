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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_autos.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_autos.md","full":"\/assn\/dj4e_autos.md"},
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
  <option value="dj4e_autos.md" selected>Login / Autos CRUD</option>
  <option value="dj4e_local.md">Installing Django Locally</option>
  <option value="dj4e_github.md">Using GitHub</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Login / Autos CRUD</h1>
<p>This assignment is to build a fully working CRUD (Create, Read, Update, and Delete)
application to manage automobiles and their makes (i.e. Ford, Hyundai, Toyota,
Tata, Audi, etc.).</p>
<p>This application will be based on this folder in the samples repo:</p>
<p><a href="https://github.com/csev/dj4e-samples/tree/master/autos">https://github.com/csev/dj4e-samples/tree/master/autos</a></p>
<p><strong>Do not clone this repository for this assignment</strong>.  You will make a new
project and application in your <code>django_projects</code> folder and use this application
as <em>sample code</em>.</p>
<p>This application will be similar to:</p>
<p><a href="https://crud.dj4e.com">https://crud.dj4e.com</a></p>
<p>The login information is as follows:</p>
<pre><code>Account: dj4e-crud
Password: dj4e_nn_!</code></pre>
<p>The 'nn' is a 2-digit number that by now, you should be able to easily guess.</p>
<h2>Making a New Application</h2>
<p>Activate any virtual environment you need (if any) and go into your <code>django_projects</code> folder
and start a new application in your <code>mysite</code> project (this project already should have the 'hello'
application from a
<a href="dj4e_hello.md">previous assignment</a>).</p>
<pre><code>workon django3  # as needed
cd ~/django_projects/mysite
python3 manage.py startapp autos</code></pre>
<h2>Extending the home (i.e. main) page</h2>
<p>Since we will build a number of applications in this project, we will use the <code>home</code>
application to provide convienent urls to switch between applications.</p>
<p>And you should have a file <code>mysite/home/templates/home/main.html</code> that has the text for the top-level page.
You can keep the &quot;Hello World&quot; text in the page somewhere.</p>
<p>Add a link to the &quot;/autos&quot; url in <code>mysite/home/templates/home/main.html</code> and anything else the autograder needs:</p>
<pre><code>&lt;li&gt;&lt;a href="/autos"&gt;Autos CRUD&lt;/a&gt;</code></pre>
<p>It is a list because we will be adding more applications in future assignments. :)</p>
<h2>Building the Autos Application</h2>
<p>The essense of this task is to adapt the code from:</p>
<p><a href="https://github.com/csev/dj4e-samples/tree/master/autos">https://github.com/csev/dj4e-samples/tree/master/autos</a></p>
<p>and make it work in your <code>autos</code> project.  As always there is a lot of code in <code>dj4e-samples</code> - be careful
copying - and only copy code when you know why you are copying it.  Go slowly.</p>
<p>Here are some tasks:</p>
<ul>
<li>
<p>Go into your <code>dj4e-samples</code> folder and do a <code>git pull</code> to get the latest version of the samples code.</p>
</li>
<li>
<p>Create <code>mysite/home/templates</code> and <code>mysite/home/templates/registration</code> folders using <code>mkdir</code> and copy the
(<a href="https://github.com/csev/dj4e-samples/blob/master/home/templates/registration/login.html" target="_blank">login.html</a>) template from <code>dj4e-samples</code> into <code>mysite/home/templates/registration/login.html</code>.</p>
</li>
<li>
<p>Copy the file from <code>dj4e-samples/home/templates/base_bootstrap.html</code> into
your <code>mysite/home/templates</code> - this will be used in your <code>autos/templates</code> and make our HTML look
better by applying the <a href="https://getbootstrap.com/docs/4.0/" target="_blank">Bootstrap</a>
and other styling libraries.</p>
</li>
<li>
<p>Edit <code>mysite/mysite/settings.py</code> add the autos application to the list of <code>INSTALLED_APPS</code>.
You can follow the pattern of the <code>HomeConfig</code> line in that file.</p>
</li>
<li>
<p>Edit <code>mysite/mysite/urls.py</code> and
add the <code>accounts/</code> path so you can use the Django built in login features.
(<a href="https://docs.djangoproject.com/en/3.0/topics/auth/default/#module-django.contrib.auth.views" target="_blank">Authentication Views</a>).
Also edit <code>mysite/mysite/urls.py</code> to route <code>autos/</code> urls to <code>autos/urls.py</code> file.</p>
<pre><code>path('accounts/', include('django.contrib.auth.urls')),  # Add
path('autos/', include('autos.urls')),                   # Add</code></pre>
</li>
<li>
<p>Edit the <code>autos/urls.py</code> file to add routes for the list, edit, and delete pages for both autos and makes</p>
</li>
<li>
<p>Edit the <code>autos/views.py</code> file to add views for the list, edit, and delete pages for both autos and makes.
It will make things a lot simpler in the long run if you convert the Make views to
the shorter form like the Auto views.
(<a href="https://github.com/csev/dj4e-samples/blob/master/autos/views.py" target="_blank">Example</a>)</p>
</li>
<li>
<p>In your <code>views.py</code> file, you should <em>not</em> simply use the code for the <code>Make</code> views.  You
should rewrite the <code>Make</code> views using the same patterns as the <code>Auto</code> views.  If you
don't use the generic edit views on your <code>Make</code> views you will need to define the
appropriate <code>MakeForm</code> in your <code>forms.py</code> just like in the sample code.  The
best approach is to build your <code>views.py</code> <em>without</em> using
a <code>forms.py</code> - but you can do it either way.</p>
</li>
<li>Edit the <code>autos/models.py</code> file to add Auto and Makes models with a foreign
key from Autos to Makes.</li>
</ul>
<img src="svg/auto_model.svg" alt="A data model diagram showing Autos and Makes" style="display: block; margin-left: auto; margin-right: auto;align: center; max-width: 300px;">
<ul>
<li>
<p>Run the <code>python3 manage.py check</code> until you see no errors</p>
</li>
<li>
<p>Run the <code>makemigrations</code> and <code>migrate</code>  commands to perform the migrations.</p>
</li>
<li>
<p>Edit <code>autos/admin.py</code> to add the Auto and Make models to the Django administration interface.</p>
</li>
<li>
<p>Create a superuser so you can test the admin interface
and log in to the application.</p>
</li>
<li>
<p>Create the necessary views in <code>autos/templates/autos</code> to support your views.
Note that the sample code uses a sub folder under <code>templates</code> to
make sure that templates are not inadvertently shared across multiple applications within a Django project.</p>
</li>
<li>
<p>Find the line in your <code>base_bootstrap.html</code> that looks like this:</p>
<pre><code>&lt;meta name="dj4e-code" content="99999999"&gt;</code></pre>
<p>and change the <code>9999999</code>  to be &quot;<span id="dj4e-code">missing</span>&quot;</p>
</li>
</ul>
<p>Make sure to check the autograder for additional markup requirements.</p>
<h2>Things that can go wrong</h2>
<p>If you ever get a 405 error on a Django page it probably means that you
have defined a view class that does not have a <code>get()</code> method.
For example if you meant to say this:</p>
<pre><code>class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')</code></pre>
<p>But instead you did:</p>
<pre><code>class AutoUpdate(LoginRequiredMixin, View):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')</code></pre>
<p>(i.e. you extended <code>View</code> instead of <code>UpdateView</code>) - the result is that there
is no <code>def get(self, request):</code> in your view.
So you get the
<a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_errors" target="_blank">405 HTTP status code</a> (invalid method)
when you navigate to the URL that forwards to the view.</p>
<h2>References</h2>
<ul>
<li>
<p><a href="https://github.com/csev/dj4e-samples/tree/master/autos" target="_blank">Autos CRUD Sample Code</a></p>
</li>
<li>
<p><a href="dj4e_install.md" target="_blank">Installing Django Locally</a></p>
</li>
<li>
<p><a href="../ngrok" target="_blank">Using ngrok to turn in your assignments</a></p>
</li>
<li><a href="https://stackoverflow.com/questions/13808020/include-an-svg-hosted-on-github-in-markdown" target="_blank">Embedding SVG in Markdown</a></li>
</ul>
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
