import * as THREE from './three.module.js';

import { StereoEffect } from './StereoEffect.js';
// container整个世界
let container, camera, scene, renderer, effect;
// 所有的球
const spheres = [];

let alpha = 0, beta=0, gamma=0;

// 一会过
window.addEventListener("deviceorientation", handleOrientation);
window.addEventListener("keydown",test);
init();
animate();
function test(event){
    switch (event.keyCode) {
        case 37:
            console.log("left")
            gamma+=10
            break;
        case 38:
            console.log('up');
            beta+=10
            break;
        case 39:
            console.log("right")
            gamma-=10
            break;
        case 40:
            console.log("down")
            beta-=10
            break;
    }
}
function test2(){
    gamma+=10
    console.log(beta,gamma)
}
function init() {
// 新增一个容器， 在html里新增了。将整个世界简历出来
    container = document.createElement( 'div' );
    document.body.appendChild( container );
// 建立一个perspectiveCamera，按照极坐标来配置， 地点，角度
    // 60是帧数。 比例 后面的1,10000是具体的精确度，以10000为基础去调整。three.js里能得到这个值。
    camera = new THREE.PerspectiveCamera( 60, window.innerWidth / window.innerHeight, 1, 100000 );
// 具体的横纵坐标 高度是3200
    camera.position.z = 3200;
// 一直到textureCube.mapping都是建立我们的背景
   // 按照正负x,正负y的顺序，拼成了一个cube设置到背景当中
    scene = new THREE.Scene();
    scene.background = new THREE.CubeTextureLoader()
        .setPath( './' )
        .load( [ 'posx.jpg', 'negx.jpg', 'posy.jpg', 'negy.jpg', 'posz.jpg', 'negz.jpg' ] );
// 是一个球，建立球的object
    const geometry = new THREE.SphereGeometry( 100, 32, 16 );
// 给cube去读取东西。 每个cube渲染会读取这个额东西。可以动态改变的东西
    const textureCube = new THREE.CubeTextureLoader()
        .setPath( './' )
        .load( [ 'posx.jpg', 'negx.jpg', 'posy.jpg', 'negy.jpg', 'posz.jpg', 'negz.jpg' ] );
// cube是每个球自己的background。 把前后左右上下的mapping关系丢进去
    textureCube.mapping = THREE.CubeRefractionMapping;
// texture是一张图。 material一开始是全白的。 envmap就是上面那个东西。 ratio是折射还是反射率。 新建一个material。 three.js里的功能叫material， 模拟什么铁片之类的。 0.95调高就是实心的球。
    const material = new THREE.MeshBasicMaterial( { color: 0xffffff, envMap: textureCube, refractionRatio: 0.95 } );
// 设置500个球
    for ( let i = 0; i < 500; i ++ ) {

        const mesh = new THREE.Mesh( geometry, material );
       //  新建xyz 圆心的地址
        mesh.position.x = Math.random() * 10000 - 5000;
        mesh.position.y = Math.random() * 10000 - 5000;
        mesh.position.z = Math.random() * 10000 - 5000;
        // 拉伸效果，调整scale的大小 一开始0-1， 所以是1-4
        mesh.scale.x = mesh.scale.y = mesh.scale.z = Math.random() * 3 + 1;
// 在整个世界里container里加这个球。
        // 第一个要加到环境里。 然后在sphere数据结构里才能做调整
        scene.add( mesh );
// 在列表里极爱这个球。
        spheres.push( mesh );

    }

    //

    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio( window.devicePixelRatio );
    // 家渲染效果把render加到container
    container.appendChild( renderer.domElement );
// 把render传到effect。把渲染的东西实例化
    effect = new StereoEffect( renderer );
    effect.setSize( window.innerWidth, window.innerHeight );

    //
// 我们的window可能会重新去调整。 所以有个resize,重新设置屏幕大小。
    window.addEventListener( 'resize', onWindowResize );

}

function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
// 调整效果的范围。 效果被应用到整个屏幕当中。 但屏幕的大小是多少，
    // 效果是否生效是哪个set scissor。
    effect.setSize( window.innerWidth, window.innerHeight );

}

// On deviceorientation event, set alpha, beta, gamma
function handleOrientation(event) {
    alpha = event.alpha;
    beta = event.beta;
    gamma = event.gamma;

}

// 每毫秒update的意思
function animate() {
// 3.js里加载动画效果
    requestAnimationFrame( animate );

    render();

}

function render() {
// 调整camera跟球的位置的。除以1000
    const timer = 0.0001 * Date.now();
// alpha没有用，计算量比较大
    // change camera position using orientation catched
   //  40跟30是调参试出来的灵敏度，负beta是反着的 所以加成负贝塔
   //  camera中心点的高度是不会变的。 头会左右转，往上下看。 但脖子不会变长的。 加了后camera是会到处跑。
    camera.position.x += ( gamma*40 - camera.position.x ) * .05;
    // camera.position.x 50;
    // console.log(camera.position.x)
    console.log(beta)
    camera.position.y += ( - beta*30 - camera.position.y ) * .05;

    // camera初始看000. perspective是个环视的摄像头。 不管怎么看， 球永远在视野当中
    camera.lookAt( scene.position );
// 让球移动起来
    for ( let i = 0, il = spheres.length; i < il; i ++ ) {
        const sphere = spheres[ i ];
       //  高度上的变化比水平的更好。 不然沿着直角三角形的移动会有点蠢， 那样是呈45度角的
        sphere.position.x = 5000 * Math.cos( timer + i );
        sphere.position.y = 5000 * Math.sin( timer + i * 1.1 );
    }

    effect.render( scene, camera );

}
// 首先init加载所有的类。 背景，纹理，材料跟球，渲染效果， 然后实例化
// 然后监听resize跟orientation
// 采集了之后就render。 每次动了后camera会调整
// alpha beta那些的范围。
// 0-160 90，-90
// 改进：在转动手机的时候，数字一直在变， 可能会变道0跟360. 一会0，一会360. x,y变化会特别剧烈。 之后可以用绝对值的参数。 0-360. 到0跟360的时候，做成180-alpha然后取绝对值