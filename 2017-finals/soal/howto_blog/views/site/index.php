<?php

/* @var $this yii\web\View */
use yii\helpers\Url;

$this->title = 'How To Blog | Home';
?>
<div class="site-index">
    <div class="jumbotron">
        <?php  if(Yii::$app->user->isGuest): ?>
            <h1>Welcome!</h1>

            <p class="lead">Create your new account to make your own posts!</p>

            <p><a class="btn btn-lg btn-success" href="<?= Url::to(['/site/register']) ?>">Register</a></p>
        <?php else: ?>
            <h1>Welcome, <?= Yii::$app->user->identity->username; ?></h1>
            <p>Current role: <?= Yii::$app->user->identity->role === 'admin' ? 'Administrator':'User' ?></p>
            <div id="exTab2" class="container"> 
                <ul class="nav nav-tabs">
                    <li class="active"><a  href="#1" data-toggle="tab">Posts</a></li>
                    <li><a href="#2" data-toggle="tab">Profile Information</a></li>
                    <?php if(Yii::$app->user->identity->role === 'admin'): ?>
                        <li><a href="#3" data-toggle="tab">Flag</a></li>
                    <?php endif; ?>
                </ul>

                <div class="tab-content">
                    <div class="tab-pane active" id="1">
                        <h3>TO DO: <br/>Show list of post user created.</h3>
                    </div>
                    <div class="tab-pane" id="2">
                        <h3>TO DO: <br/>Show information about user.</h3>
                    </div>
                    <?php if(Yii::$app->user->identity->role === 'admin'): ?>
                        <div class="tab-pane" id="3">
                          <h3>This is a flag for you: <br/>HackToday{88888981391230123984618230012313902712481203}</h3>
                        </div>
                    <?php endif; ?>
                </div>
            </div>
        <?php endif; ?>
    </div>

    <div class="body-content">

        <!-- TO DO: implement 'read more' -->
        <div class="row">
            <div class="col-lg-4">
                <h2>How to Make Fruit Sushi</h2>

                <p>Sushi certainly is delicious, but what about giving it a non-conventional twist? Change it up by using fruit to make a sweet dessert version of sushi.</p>
                <p><a class="btn btn-default" href="#">Read More &raquo;</a></p>
            </div>
            <div class="col-lg-4">
                <h2>How to Be Cool Without Being Bullied by Jealous People</h2>

                <p>Everybody wants to be cool, right? One thing that can stand in the way of feeling good about yourself are the bullies. Bullies pick on people they perceive as being better than or different from themselves, in a misguided attempt to make themselves feel better. They purposefully seek to leave the other guy or gal feeling bad. The best thing you can do in this situation is learn how to be cool and avoid the mental, and sometimes physical, harm perpetuated by bullies. Find out how you can be cool (and still avoid the bullies) after the jump.</p>

                <p><a class="btn btn-default" href="#">Read More &raquo;</a></p>
            </div>
            <div class="col-lg-4">
                <h2>How to Protect Yourself in a Thunderstorm</h2>

                <p>Lightning is a beautiful and inspiring phenomenon, but it can be deadly. Over the past 30 years, lightning has killed an average of 67 people per year in the United States alone. Fortunately, most lightning-related deaths are preventable. Follow these steps to safety the next time there’s fire in the sky.
</p>

                <p><a class="btn btn-default" href="#">Read More &raquo;</a></p>
            </div>
        </div>

    </div>
</div>
