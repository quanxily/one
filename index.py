from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>小櫻喜個人網站</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style type="text/css">
        nav {
            background-color: beige;
            display: flex;
            justify-content: space-between;
            align-items: center;
            overflow: hidden;
            padding: 0 10px;
        }

        .nav-left {
            font-size: 17px;
            color: black;
            text-decoration: underline pink 20%;
        }

        .nav-right {
            display: flex;
        }

        nav a.active {
            background-color: beige;
            color: black;
        }
        
        .nav-right a {
            display: block;
            padding: 14px 16px;
            text-decoration: none;
            color: black;
            text-align: center;
            font-size: 17px;
            text-shadow: 2px 2px pink;
        }

        @media (max-width: 800px) {
            .nav-right a:not(:first-child) {
                display: none;
            }
            .nav-right a.icon {
                float: right;
                display: block;
            }
        }

        @media (max-width: 600px) {
            .nav-right.responsive {
                position: relative;
            }
            .nav-right.responsive a.icon {
                position: absolute;
                right: 0;
                top: 0;
            }
            .nav-right.responsive a {
                float: none;
                display: block;
                text-align: right;
            }
        }
         @media (max-width: 600px) {
         .grid-container{
                flex-direction: column;
                -webkit-flex-direction: column;
         }
        }
                

         @media (max-width: 400px) {
         .grid-container{
                flex-direction: column;
                -webkit-flex-direction: column;
         }
        }

         @media screen and (max-width: 768px) {
          .grid-container {
            grid-template-areas: 
              'header'
              'nav'
              'left'
              'middle'
              'right'
              'footer';
          }

          .left, .middle, .right {
            grid-area: unset;
          }
        }

        /* Responsive layout for even smaller screens */
        @media screen and (max-width: 480px) {
          .grid-container {
            grid-template-areas: 
              'header'
              'nav'
              'middle'
              'right' /* Changed the order to ensure "right" comes before "footer" */
              'footer';
          }

          .left, .middle, .right {
            margin: 0;
          }

          .left {
            display: none; /* Hiding the left and right sections on smaller screens */
          }
        }

        /* Slideshow container */
        .slideshow-container {
            position: relative;
            max-width: 1000px;
            margin: auto;
        }

        .mySlideshows {
            display: none;
        }

        .fade {
            animation-name: fade;
            animation-duration: 1.5s;
        }

        @keyframes fade {
            from {opacity: .4} 
            to {opacity: 1}
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            padding: 16px;
            margin-top: -22px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            border-radius: 0 3px 3px 0;
            user-select: none;
        }

        .next {
            right: 0;
            border-radius: 3px 0 0 3px;
        }

        .prev:hover, .next:hover {
            background-color: rgba(0,0,0,0.8);
        }


        .text {
            color: #f0970a;
            font-size: 35px;
            padding: 50px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
        }

        .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active, .dot:hover {
            background-color: #717171;
        }

       #myTop {
            display: none; /* Hidden by default */
            position: fixed; /* Fixed position */
            bottom: 20px; /* Place the button at the bottom of the page */
            right: 30px; /* Place the button 30px from the right */
            z-index: 99; /* Make sure it does not overlap */
            border: none; /* Remove borders */
            outline: none; /* Remove outline */
            background-color: pink; /* Set a background color */
            color: black; /* Text color */
            cursor: pointer; /* Add a mouse pointer on hover */
            padding: 15px; /* Some padding */
            border-radius: 25px; /* Rounded corners */
            font-size: 18px; /* Increase font size */
        }

        #myTop:hover {
            background-color: beige; /* Add a dark-grey background on hover */
        }

        footer {
            grid-area: footer;
            padding: 5px;
            text-align: center;
            background-color:beige;
        }

        footer a{
            padding: 10px;
            text-align: center;
            text-decoration: none;
            font-size: 25px;
        }

        footer a:hover {
            color: pink;
        }

         .grid-container {
            display: grid;
            grid-template-areas: 
            'nav nav nav nav nav nav'
            'header header header header header header'
            'left left middle middle right right'
            'footer footer footer footer footer footer';
            grid-gap: 5px 5px;

        }

        header {
            grid-area: header;
        }
        nav {
            grid-area: nav;
        }

        .left, .middle, .right {
            padding: 10px;
            margin: 10px;
        }

        .left {
            grid-area: left;
            background-color: #fad7d7;
            border-left: solid 20px #faabaa;
            border-radius: 10px;
        }

        .middle {
            grid-area: middle;
            background-color:#f7e8dd;
            border-radius: 10px;
        }

        .right {
            grid-area: right;
            background-color: #fad7d7;
            border-top: solid 20px #faabaa;
            border-bottom: solid 20px #faabaa;
            border-radius: 10px;
        }

        h3 {
           text-decoration: underline #f7e8dd 20%; 
        }

       .hidden-content {
            display: none;
        }
        .show-button {
            cursor: pointer;
            color: blue;
            text-decoration: underline;
        }

        .highlight {
            background-color: beige ; /* 你可以根據需要更改顏色 */
            padding: 10px;
            margin-bottom: 5px;
        }
    </style>
     <script>
       function toggleContent(buttonId, contentId) {
            const content = document.getElementById(contentId);
            const button = document.getElementById(buttonId);
            if (content.style.display === 'none' || content.style.display === '') {
                content.style.display = 'block';
                button.innerText = '隱藏';
            } else {
                content.style.display = 'none';
                button.innerText = '繼續閱讀';
            }
        }    
    </script>
</head>

<body>
   <main class="grid-container">
    <button onclick="topFunction()" id="myTop" title="Go to top">Top</button>

    <script>
        // Get the button
        var mybutton = document.getElementById("myTop");

        // When the user scrolls down 20px from the top of the document, show the button
        window.onscroll = function() {
            scrollFunction();
        };

        function scrollFunction() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                mybutton.style.display = "block";
            } else {
                mybutton.style.display = "none";
            }
        }

        // When the user clicks on the button, scroll to the top of the document
        function topFunction() {
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
        }
    </script>
    <nav id="myTopnav" class="topnav">
        <div class="nav-left"><i class="fa-solid fa-person-dress"></i>小櫻喜個人網站</div>
        <div class="nav-right" id="nav-right">
            <a href="/" class="active"><i class="fa-solid fa-briefcase"></i>工作經驗</a>
            <a href="/photo2"><i class="fa-solid fa-school"></i>學校生活</a>
            <a href="/photo3"><i class="fa-brands fa-gratipay"></i>興趣愛好</a>
            <a href="/play"><i class="fa-solid fa-address-book"></i>作品與證照</a>
            <a href="javascript:void(0);" class="icon" onclick="navFunction()">&#9776;</a>
        </div>
    </nav>

       <header class="slideshow-container">
        <div class="mySlideshows fade">
            <img src="static/428.jpg" style="width: 100%; height: 500px;" >
            <div class="text">國中的我-1</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/112.jpg" style="width: 100%; height: 500px;">
            <div class="text">高中的我 - 2</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/113.jpg" style="width: 100%; height: 500px;">
            <div class="text">大學的我 - 3</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/14.jpg" style="width:100%; height: 500px;">
            <div class="text">人生語錄 - 4</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/15.jpg" style="width: 100%;  height: 500px;">
            <div class="text">愛情語錄 - 5</div>
        </div>

        <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
        <a class="next" onclick="plusSlides(1)">&#10095;</a>

        <div style="text-align: center;">
            <span class="dot" onclick="currentSlide(1)"></span>
            <span class="dot" onclick="currentSlide(2)"></span>
            <span class="dot" onclick="currentSlide(3)"></span>
            <span class="dot" onclick="currentSlide(4)"></span>
            <span class="dot" onclick="currentSlide(5)"></span>
        </div>
    </header>

     <script>
        function navFunction() {
            var x = document.getElementById("nav-right");
            if (x.className === "nav-right") {
                x.className += " responsive";
            } else {
                x.className = "nav-right";
            }
        }

        let slideIndex = 1;
        showSlides(slideIndex);

        function plusSlides(n) {
            showSlides(slideIndex += n);
        }

        function currentSlide(n) {
            showSlides(slideIndex = n);
        }

        function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("mySlideshows");
            let dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}
            if (n < 1) {slideIndex = slides.length}
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex-1].style.display = "block";
            dots[slideIndex-1].className += " active";
        }
    </script>

        <hr>

        <aside class="left">

                        <h3><i class="fa-solid fa-paw"></i>關於我</h3>
                        <p>我是一個</p>


                 
                        <h3><i class="fa-solid fa-paw"></i>工作經驗</h3>
                        <p>
                            我的工作有跨不同的行業,便利商店,腳踏車零件工廠,彩券行,會做那麼多是因為想要多存錢靠自己不讓父母擔心,且做的性質不同,我的第一份是暑期工讀,後面兩份都是做長期的工讀,
                            <span id="toggleButton1" class="show-button" onclick="toggleContent('toggleButton1', 'moreContent1')">繼續閱讀</span>
                        </p>
                        <div id="moreContent1" class="hidden-content">
                            <p>
                                想要了解更詳細內容,請點擊後面連結,
                                <a href="/" ><i class="fa-solid fa-briefcase"></i>工作經驗</a>
                            </p>
                        </div>
                    

                    
                        <h3><i class="fa-solid fa-paw"></i>學校生活</h3>
                        <p>
                            我在學校人脈不多,沒有什麼朋友,也沒有去參加社團,就是上學上課而已,直到一件事情的發生改變了我的生活和思維
                            <span id="toggleButton2" class="show-button" onclick="toggleContent('toggleButton2', 'moreContent2')">繼續閱讀</span>
                        </p>
                        <div id="moreContent2" class="hidden-content">
                            <p>
                                想要了解更詳細內容,請點擊後面連結,
                                <a href="/" ><i class="fa-solid fa-briefcase"></i>學校生活</a>
                            </p>
                        </div>
                

                   
                        <h3><i class="fa-solid fa-paw"></i>興趣愛好</h3>
                        <p>
                            我在學校人脈不多,沒有什麼朋友,也沒有去參加社團,就是上學上課而已,但是我會利用空檔時間去做我喜歡做的事情或者是能夠讓我有趕到成就感的事情
                            <span id="toggleButton3" class="show-button" onclick="toggleContent('toggleButton3', 'moreContent3')">繼續閱讀</span>
                        </p>
                        <div id="moreContent3" class="hidden-content">
                            <p>
                                想要了解更詳細內容,請點擊後面連結,
                                <a href="/" ><i class="fa-solid fa-briefcase"></i>興趣愛好</a>
                            </p>
                        </div>
                  

                   
                        <h3><i class="fa-solid fa-paw"></i>證照與作品</h3>
                        <p>
                            我在學校人脈不多,沒有什麼朋友,也沒有去參加社團,就是上學上課而已,等到升大二下才知道原來證照的作用也考到了第一張技術證照
                            <span id="toggleButton4" class="show-button" onclick="toggleContent('toggleButton4', 'moreContent4')">繼續閱讀</span>
                        </p>
                        <div id="moreContent4" class="hidden-content">
                            <p>
                                想要了解更詳細內容,請點擊後面連結,
                                <a href="/" ><i class="fa-solid fa-briefcase"></i>證照與作品</a>
                            </p>
                        </div>
                    
         </aside>

        <section class="middle">
            <h2>姓名：楊荃喜</h2>
            <h2>學校：靜宜大學</h2>
            <h2>星座：水瓶座</h2>
            <h2>興趣：</h2>
            <h2>專長：做網頁</h2>
            <h2>科系：資管系</h2>
            <h2>當初選擇本科系的原因：</h2>
            <h2>作品：此網站是一個還有另外兩個網站</h2>
            <h2>證照：ERP軟體規畫師</h2>
            <h2>考取證照的原因：</h2>
            <h2>有成就感的事情：看著自己做的網頁一步步變得越來越好看</h2>
            <h2>做網頁遇到的挫折：</h2>
            <h2>解決問題的方式：</h2>
        </section>

        <aside class="right">
           
                <h3><i class="fa-solid fa-film"></i>現今目標</h3>
                    <p class="highlight"><i class="fa-regular fa-money-bill-1"></i>存款至少3萬</p>
                    <p class="highlight">考到ERP　Ｃ級證照一張</p>
                    <p class="highlight">做出專屬於自己的網站</p>
          
           
                <h3><i class="fa-solid fa-film"></i>五年後目標</h3>
                <p class="highlight"><i class="fa-regular fa-money-bill-1"></i>存款至少２０萬</p>
                <p class="highlight">有足夠的錢與愛人一起出國旅遊</p>
                <p class="highlight">改換跑道做業務行工作</p>
           
           
             <h3><i class="fa-solid fa-film"></i>十年後目標</h3>
             <p class="highlight">讓身邊的人都接觸賀寶芙</p>
            　<p class="highlight">讓自己的身體維持健康</p>
            　<p class="highlight">與自己的愛人規劃長久的旅行</p>
          

        </aside>
    </main>
    <footer>
        <a href="https://www.instagram.com/quanxily/"><i class="fa-brands fa-instagram-square"></i>Ig</a>
        <h3>Copyright ©  楊荃喜. All Rights Reserved.</h3>
    </footer>
</body>
</html>
"""


@app.route("/")
def index():
    x = html
    return x


@app.route("/photo2")
def photo2():
    return render_template("photo2.html")

@app.route("/play")
def play():
    return render_template("play.html")


@app.route("/photo3")
def photo3():
    return render_template("photo3.html")


#if __name__ == "__main__":
# app.run()