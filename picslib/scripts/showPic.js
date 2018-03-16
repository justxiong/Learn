//分离js: 事件可以不在html文档中处理，在js文件中动态添加
//对象检测：几乎所有东西都可以当成对象来检测,可以增加脚本兼容性，if(!object)return false;
/*性能考虑：查询dom，浏览器会查找整个dom树，尽量减少dom访问，减少元素标记
    尽量将脚本合并，减少加载时发送请求数量，<script>放在head会影响其他文件加载，因此最好将<script>放置后面
*/

window.onload = prepareLinks;

function prepareLinks() {
    //对象检测
    if (!document.getElementsByTagName) return false;
    links = document.getElementsByTagName("a");
    for (link of links) {
        if (link.getAttribute("class") === "popup") {
            //动态添加事件实现js/html分离
            link.onclick = function() {
                //showPic(this);
                popUp(this.getAttribute("href"));
                return false;
            }
        }
    }
}

function popUp(winURL) {
    window.open(winURL, "popup", "width=320,height=480");
}

function showPic(whichpic) {
    var source = whichpic.getAttribute("href");
    var placeholder = document.getElementById('placeholder');
    var text = whichpic.getAttribute("title");
    var description = document.getElementById("description");
    placeholder.setAttribute('src', source);
    description.innerHTML = text;

}