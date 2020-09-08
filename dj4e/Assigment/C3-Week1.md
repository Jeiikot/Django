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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_hello.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_hello.md","full":"\/assn\/dj4e_hello.md"},
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
  <option value="dj4e_hello.md" selected>Hello Session World</option>
  <option value="dj4e_load.md">Batch Loading Data</option>
  <option value="dj4e_autos.md">Login / Autos CRUD</option>
  <option value="dj4e_local.md">Installing Django Locally</option>
  <option value="dj4e_github.md">Using GitHub</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>DIY: Hello World / Sessions</h1>
<p>In this application, you will make a new application in your <code>django_projects</code>
and add a bit of code to make use of sessions.  A key element of this assignment is
that we will tell you &quot;what to do&quot; and less exact steps to cut and paste.  It is time
for you to understand how to &quot;Do It Yourself&quot; (DIY).</p>
<p>This assignment will not have any models - just views.  In this assignment you will
be looking at the <code>dj4e-samples</code> code and figuring out how to read and adapt sample code.
You should make sure to get the latest updates by doing the following:</p>
<pre><code>cd ~/dj4e-samples
git pull</code></pre>
<p>Be very careful pulling code from <code>dj4e-samples</code> - it often has much more
code than your program needs - so know what you are looking at before you copy
code into your application.</p>
<h2>Building a Main Page</h2>
<p>It is time for your the &quot;/&quot; URL in your application to actually refer to a real page instead
of throwing a &quot;404 Not Found&quot; error.  We will store this page (and other project-wide
bits) in an application named &quot;home&quot;.  To get started:</p>
<pre><code>workon django3                  # as needed
cd ~/django_projects/mysite
python3 manage.py startapp home</code></pre>
<p>Create an HTML file in <code>~/django_projects/mysite/home/templates/home/main.html</code> with the following HTML:</p>
<pre><code>&lt;ul&gt;
&lt;li&gt;&lt;p&gt;&lt;a href="/polls"&gt;A Polls Application&lt;/a&gt;&lt;/p&gt;&lt;/li&gt;
&lt;/ul&gt;</code></pre>
<p>You can add more HTML - but this list and links should be somewhere in the template.</p>
<p>Edit the file <code>~/django_projects/mysite/mysite/urls.py</code> and add following path route:</p>
<pre><code>path('', TemplateView.as_view(template_name='home/main.html')),</code></pre>
<p>You will need to make sure to add the proper python imports at the top of the file to make this work.
There are lots of examples of the use of TemplateView in the <code>urls.py</code> files in <code>dj4e-samples</code>
and in the lecture materials.</p>
<p>Edit the file <code>~/django_projects/mysite/mysite/settings.py</code> and add the <code>home</code> application following
the pattern that you used to add the <code>polls</code> application to <code>INSTALLED_APPS</code>;</p>
<p>Make sure to run:</p>
<pre><code>python3 manage.py check</code></pre>
<p>To see if your changes have syntax errors, then Reload your web application and
navigate to the top level path (i.e. no path).  You should no longer
get a &quot;404&quot; and instead be able to navigate to the polls application by clicking on the link.
Congratulations!  You now have a web site that is not broken.</p>
<p>Note that this page is not present on the <a href="https://djtutorial.dj4e.com/" target="_blank">
<a href="https://djtutorial.dj4e.com/">https://djtutorial.dj4e.com/</a></a> server.  It still shows &quot;404&quot; when you navigate to the top URL.</p>
<h2>Playing With Sessions (DIY)</h2>
<p>You next goal is to make a new application named <code>hello</code> and replicate the functionality
at <a href="https://samples.dj4e.com/session/sessfun">https://samples.dj4e.com/session/sessfun</a> except make it so that it responds to the
URL <code>/hello</code> in your Django project like in <a href="https://djtutorial.dj4e.com/hello" target="_blank">
<a href="https://djtutorial.dj4e.com/hello">https://djtutorial.dj4e.com/hello</a></a></p>
<p>Add a link to <code>~/django_projects/mysite/home/templates/home/main.html</code> with the following HTML:</p>
<pre><code>&lt;li&gt;&lt;p&gt;&lt;a href="/hello"&gt;Test the session&lt;/a&gt;&lt;/p&gt;</code></pre>
<p>This is the DIY part of this assignment - no more cutting and pasting instructions :)</p>
<p>There is lots of sample code in <code>dj4e-samples</code> - probably
too much code.  If you just copy and paste everything from <code>dj4e-samples</code> it will be difficult to
make this work.  Sometime when looking at code written by others, it is important to know what
is going on to what <em>not</em> to copy.</p>
<p>Also make sure to check any auto grader for any additional requirements for this assignment.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
