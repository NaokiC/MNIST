(function(e){function t(t){for(var r,o,l=t[0],c=t[1],s=t[2],p=0,f=[];p<l.length;p++)o=l[p],Object.prototype.hasOwnProperty.call(a,o)&&a[o]&&f.push(a[o][0]),a[o]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(e[r]=c[r]);u&&u(t);while(f.length)f.shift()();return i.push.apply(i,s||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],r=!0,l=1;l<n.length;l++){var c=n[l];0!==a[c]&&(r=!1)}r&&(i.splice(t--,1),e=o(o.s=n[0]))}return e}var r={},a={app:0},i=[];function o(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=r,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],c=l.push.bind(l);l.push=t,l=l.slice();for(var s=0;s<l.length;s++)t(l[s]);var u=c;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("85ec")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("ImageGetter",{attrs:{msg:"Welcome to Your Vue.js App"}})],1)},i=[],o=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("h1",[e._v("MNIST Classifier")]),n("h2",[e._v("You can drop one image with a digit")]),n("div",{staticClass:"helper"}),n("div",{staticClass:"drop display-inline align-center",on:{dragover:function(e){e.preventDefault()},drop:e.onDrop}},[n("div",{staticClass:"helper"}),e.image?n("div",{staticClass:"hidden display-inline align-center",class:{image:!0}},[n("img",{staticClass:"img",attrs:{src:e.image,alt:""}}),n("br"),n("br"),n("button",{staticClass:"btn",on:{click:e.removeFile}},[e._v("REMOVE")]),n("button",{staticClass:"btn",on:{click:e.sendFile}},[e._v("SEND")])]):n("label",{staticClass:"btn display-inline"},[e._v(" SELECT OR DROP AN IMAGE "),n("input",{attrs:{type:"file",name:"image"},on:{change:e.onChange}})])])])},l=[],c=(n("ac1f"),n("466d"),n("bc3a")),s=n.n(c),u={data:function(){return{image:""}},methods:{onDrop:function(e){e.stopPropagation(),e.preventDefault();var t=e.dataTransfer.files;this.createFile(t[0])},onChange:function(e){var t=e.target.files;this.createFile(t[0])},createFile:function(e){if(e.type.match("image.*")){var t=new FileReader,n=this;t.onload=function(e){n.image=e.target.result},t.readAsDataURL(e)}else alert("Select an image")},removeFile:function(){this.image=""},sendFile:function(){s.a.defaults.headers.common["Access-Control-Allow-Origin"]="*";var e=JSON.stringify({image:this.image}),t={method:"post",url:"http://localhost:5000/",headers:{"Content-Type":"application/json"},data:e};console.log(e),s()(t).then((function(e){console.log(JSON.stringify(e.data))})).catch((function(e){console.log(e)}))}}},p=u,f=(n("8d94"),n("2877")),d=Object(f["a"])(p,o,l,!1,null,null,null),g=d.exports,h={name:"App",components:{ImageGetter:g}},v=h,m=(n("034f"),Object(f["a"])(v,a,i,!1,null,null,null)),b=m.exports;r["a"].config.productionTip=!1,new r["a"]({render:function(e){return e(b)}}).$mount("#app")},"85ec":function(e,t,n){},"865e":function(e,t,n){},"8d94":function(e,t,n){"use strict";n("865e")}});
//# sourceMappingURL=app.1087dbf2.js.map