<template>
  <div>
    <h1>MNIST Classifier</h1>
    <h2>You can drop one image with a digit</h2>
    <div class="helper"></div>
    <div class="drop display-inline align-center" @dragover.prevent @drop="onDrop">
      <div class="helper"></div>
      <label v-if="!image" class="btn display-inline">
        SELECT OR DROP AN IMAGE
        <input type="file" name="image" @change="onChange">
      </label>
      <div class="hidden display-inline align-center" v-else v-bind:class="{ 'image': true }">
        <img :src="image" alt="" class="img" />
        <br>
        <br>
        <button class="btn" @click="removeFile">REMOVE</button>
        <button class="btn" @click="sendFile">SEND</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      image: ''
    }
  },
  methods: {
    onDrop(e) {
      e.stopPropagation();
      e.preventDefault();
      let files = e.dataTransfer.files;
      this.createFile(files[0]);
    },
    onChange(e) {
      let files = e.target.files;
      this.createFile(files[0]);
    },
    createFile(file) {
      if (!file.type.match('image.*')) {
        alert('Select an image');
        return;
      }
      //let img = new Image();
      let reader = new FileReader();
      let vm = this;

      reader.onload = function(e) {
        vm.image = e.target.result;
      }
      reader.readAsDataURL(file);
    },
    removeFile() {
      this.image = '';
    },
    sendFile() {
      axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

      let data = JSON.stringify({"image":this.image});

      let config = {
        method: 'post',
        url: 'http://0.0.0.0:5000/',
        headers: {
          'Content-Type': 'application/json'
        },
        data : data
      };

      console.log(data)

      axios(config)
          .then(function (response) {
            console.log(JSON.stringify(response.data));
          })
          .catch(function (error) {
            console.log(error);
          });
    }
  }

}

</script>

<style>

*,
*:after,
*:before {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  -webkit-touch-callout: none;
}


html, body {
  height: 100%;
  text-align: center;
}

.btn {
  background-color: #d3394c;
  border: 0;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-weight: bold;
  padding: 15px 35px;
  position: relative;
}

.btn:hover {
  background-color: #722040;
}

input[type="file"] {
  position: absolute;
  opacity: 0;
  z-index: -1;
}

.align-center {
  text-align: center;
}


.helper {
  height: 100%;
  display: inline-block;
  vertical-align: middle;
  width: 0;
}

.hidden {
  display: none !important;
}

.hidden.image {
  display: inline-block !important;
}

.display-inline {
  display: inline-block;
  vertical-align: middle;
}

.img {
  border: 1px solid #f6f6f6;
  display: inline-block;
  height: auto;
  max-height: 80%;
  max-width: 80%;
  width: auto;
}

.drop {
  border: 4px dashed #ccc;
  background-color: #f6f6f6;
  border-radius: 2px;
  height: 400px;
  max-height: 400px;
  max-width: 600px;
  width: 100%;
}
</style>
