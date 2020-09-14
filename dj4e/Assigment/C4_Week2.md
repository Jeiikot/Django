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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_ads2.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_ads2.md","full":"\/assn\/dj4e_ads2.md"},
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
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md" selected>AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Classified Ad Web Site - Milestone 2</h1>
<p>In this assignment, you will expand your classified ads web site to add functionality
equivalent to:</p>
<p><a href="https://chucklist.dj4e.com/m2">https://chucklist.dj4e.com/m2</a></p>
<p>The primary additions from the previous milestone are to add an image to each ad
and add comments for each ad.</p>
<p>You will build this application by borrowing parts and pieces from the code that runs</p>
<p><a href="https://samples.dj4e.com/">https://samples.dj4e.com/</a></p>
<p>and combining them into a single application.</p>
<h2>Adding Pictures to the Ads Application</h2>
<p>In this section, you will pull bits and pieces of the <code>pics</code> sample application
into your <code>ads</code> application to add support for an optional single picture per ad.</p>
<p>(1) Add this to your <code>ads/model.py</code>, talking inspiration from <code>dj4e-samples/pics/models.py</code></p>
<pre><code>class Ad(models.Model) :

    ...
    # Picture
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    ...</code></pre>
<p>Do not include the entire <code>Pic</code> model.  Of course do the migrations once you have modified the model.</p>
<p>(2) Copy in the <code>pics/forms.py</code> as well as <code>pics/humanize.py</code>.</p>
<p>(3) Take a look at <code>pics/views.py</code> and adapt the patterns in <code>PicCreateView</code> and
<code>PicUpdateView</code> and replace the code for <code>AdCreateView</code> and <code>AdUpdateView</code> in <code>ads/views.py</code>.
These new views don't inherit from owner.py becuase they manage the <code>owner</code> column in the <code>get()</code>
and <code>put()</code> methods.</p>
<p>(4) Alter your <code>templates/ads/ad_form.html</code> by looking through <code>pics/templates/pics/form.html</code>.  Make sure to add the
JavaScript bits at the end and add <code>enctype="multipart/form-data"</code> and the <code>id</code>
attribute to the <code>form</code> tag.</p>
<p>(5) Alter the <code>templates/ads/ad_detail.html</code> template by looking through <code>pics/templates/pics/detail.html</code> and
to add code to include the image in the output if there is an image associated with the ad.
Make sure not to lose the <code>price</code> field in your UI.  If you don't see the <code>price</code> field
in your UI it is likely a mistake in your <code>forms.py</code>.</p>
<p>(6) Add a <code>ad_picture</code> route to your <code>urls.py</code> based on the <code>pics_picture</code> route from <code>pics/urls.py</code>:</p>
<pre><code>path('ad_picture/&lt;int:pk&gt;', views.stream_file, name='ad_picture'),</code></pre>
<p>(5) Add the <code>stream_file()</code> view from <code>pics/views.py</code> and adapt appropriately</p>
<p>Test to make sure you can upload, view, and update pictures with your ads.</p>
<h2>Adding Comments to the Ads Application</h2>
<p>In this section, you will pull bits and pieces of the <code>forum</code> sample application
into your <code>ads</code> application to add support for comments for each ad.</p>
<p>(1) Update your <code>models.py</code> adding the comment feature from the <code>forums/models.py</code></p>
<pre><code>class Ad(models.Model) :

    ...
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Comment', related_name='comments_owned')
    ...

class Comment(models.Model) :
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) &lt; 15 : return self.text
        return self.text[:11] + ' ...'</code></pre>
<p>Do not add the Forum model - simply connect the <code>Comment</code> model to the <code>Ad</code> model. Of course do
the migrations once you have modified the model successfully.</p>
<p>(2) Pull the <code>CommentForm</code> class from <code>forums/forms.py</code> into your <code>forms.py</code>.</p>
<p>(3) Adapt the <code>get()</code> method from <code>ForumDetailView</code> to your <code>AdDetailView</code> to retrieve the list of comments
and create the <code>CommentForm</code> and pass them into your
<code>templates/ads/ad_detail.html</code> template through the context.</p>
<p>(4) Adapt the <code>templates/ads/ad_detail.html</code> template to show comments and show a delete icon
when a comment belongs to the current logged in user.</p>
<p>(5) Also add the ability to add a comment to an ad in <code>ad_detail.html</code> when the user is logged in by looking
at the techniques in <code>forums/templates/forums/detail.html</code>.</p>
<p>(6) Add a route in <code>urls.py</code> for the <code>ad_comment_create</code> and <code>ad_comment_delete</code>
routes from <code>forums/urls.py</code>.  Make sure to use the same URL patterns as shown here:</p>
<pre><code>urlpatterns = [
    ...
    path('ad/&lt;int:pk&gt;/comment',
        views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/&lt;int:pk&gt;/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('ads')), name='ad_comment_delete'),
]</code></pre>
<p>(7) Adapt the comment related views from <code>forums/views.py</code> and put them into your <code>view.py</code>.</p>
<p>(8) You will have to adapt the <code>forums/templates/forums/comment_delete.html</code> template to work in your ads application.</p>
<h2>Do Some or All of the Challenges</h2>
<p>You will have to finish these by the next assignment - so you might as well work on them now.
And they are fun.</p>
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
use localhost, you probably will get the <code>The redirect_uri MUST match the registered callback URL for this application.</code> error message when you use social login.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
<script>
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
