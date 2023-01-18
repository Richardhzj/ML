import {
	StereoCamera,
	Vector2
} from 'three';

class StereoEffect {
	// 球的背景能是 flash effect
	constructor( renderer ) {

		// has two perspectiveCamera: .cameraL, .cameraR
		const _stereo = new StereoCamera();
		_stereo.aspect = 0.5;
		const size = new Vector2();
		// distance between eyes   default eyeSep is 0.064
		this.setEyeSeparation = function ( eyeSep ) {

			_stereo.eyeSep = eyeSep;

		};

		this.setSize = function ( width, height ) {

			renderer.setSize( width, height );

		};
// 背景虚化渲染
		this.render = function ( scene, camera ) {
//上面抓取球。 把scene跟camera传进去
			// 采集了背景后面的图片。 所以是个透明的。
//			auto update会自动更新 镜头自动更新。 球有移动会更新
//			光穿透了object，
//			light->object 挡住后面的background 现在让object自己变成background color 自己颜色改成scene的颜色。 从而实现光穿透object打到background 透明的效果。。 render会有波动混沌的效果
			if ( scene.matrixWorldAutoUpdate === true ) scene.updateMatrixWorld();
//camera调用3.js相关的镜头。 scene跟camer会自动更新
			if ( camera.parent === null && camera.matrixWorldAutoUpdate === true ) camera.updateMatrixWorld();
//加上渲染的两个类， 球的size 拿到大小。 把球里的图片清掉
			_stereo.update( camera );

			renderer.getSize( size );
//裁剪背后的图片
			if ( renderer.autoClear ) renderer.clear();
			renderer.setScissorTest( true );
//把左半部分跟右半部分分别做了渲染
			renderer.setScissor( 0, 0, size.width / 2, size.height );
			renderer.setViewport( 0, 0, size.width / 2, size.height );
			renderer.render( scene, _stereo.cameraL );
//最后把effect输出出来
			renderer.setScissor( size.width / 2, 0, size.width / 2, size.height );
			renderer.setViewport( size.width / 2, 0, size.width / 2, size.height );
//			渲染新的球
			renderer.render( scene, _stereo.cameraR );

			renderer.setScissorTest( false );

		};

	}

}

export { StereoEffect };