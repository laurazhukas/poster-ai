<template>
  <transition name="new-survey">
    <div style="text-align: center">

      <!-- File uploading -->
      <transition name="next">
        <div v-if="uploading">
          <!-- File upload component - Drag'n'drop enabled for this entire space -->
          <file-upload class="file-upload"
            :multiple="true"
            ref="upload"
            :drop="true"
            v-model="files"
            @input-filter="inputFilter">
            <div class="upload-space-hover font-weight-light headline" v-if="$refs.upload && $refs.upload.dropActive">
              Drop to Upload
            </div>
            <div class="upload-space font-weight-light headline" v-else>
              Drag and Drop (Or click)
            </div>
          </file-upload>

          <!-- Display the images uploaded -->
          <transition name="new-survey">
            <v-card style="width: 90%; margin: auto">
              <div class="img-container" v-show="displayCard">
                <transition-group name="new-image">
                  <img v-for="(file, i) in files" :key="i" :src="file.url" style="max-height: 90px">
                </transition-group>
              </div>
            </v-card>
          </transition>

          <!-- Controls for continuing -->
          <transition name="new-survey">
            <v-btn id="continue" large v-if="displayCard" @click="startEval" style="margin-top: 20px">Continue and Enable Webcam</v-btn>
            <v-btn disabled id="disabled">Add Images to Continue</v-btn>
          </transition>
          <transition name="new-survey">
            <v-slider id="slide" v-if="displayCard" v-model="userCount" thumb-label="always" :min="1" :max="25" class="slider-styles"/>
          </transition>
          <transition name="new-survey">
            <div v-if="displayCard" class="font-weight-medium subheading">Number of Users</div>
          </transition>
        </div>
      </transition>


      <!-- Evaluation -->
      <transition name="next">
        <div v-if="evaluating" class="evaluation">
          <!-- Display user ID -->
          <div class="subheading font-weight-light">User {{evaluatingUser + 1}}</div>

          <!-- Image -->
          <div><img :src="files[evalIndex].url" style="max-height: 400px"></div>

          <!-- Upload button -->
          <v-btn @click="capture" :disabled="hasReacted">Capture Reaction</v-btn>

          <!-- Like/dislike -->
          <div>
            <v-btn color="error" @click="dislike" :disabled="!hasReacted">Dislike</v-btn>
            <v-btn color="success" @click="like" :disabled="!hasReacted">Like</v-btn>
          </div>

        </div>
      </transition>

      <transition name="next">
        <div v-if="processing" class="evaluation">
          <div class="headline font-weight-light font-italic">Processing results... Pretty graphs incoming soon!</div>

          <!-- Progress Spinner! -->
          <v-progress-circular indeterminate :size="100" :width="10" />

        </div>
      </transition>

      <transition name="next">
        <div v-if="hasResults" class="evaluation">
          <div class="headline font-weight-light font-italic">Processing Complete!</div>

          <!-- Maybe a fancy checkmark animation :) -->

          <v-btn :to="resultsURL">View Results</v-btn>
          
        </div>
      </transition>

      <video v-show="false" ref="video" id="video" width="640" height="480" autoplay></video>
      <canvas v-show="false" ref="canvas" id="canvas" width="640" height="480"/>
      
    </div>
  </transition>
</template>

<script>
import axios from 'axios';
import FileUpload from 'vue-upload-component';
const uuidv1 = require('uuid/v1');

export default {
  name: 'survey',
  components: { FileUpload },
  data() {
    return {
      uploadImagesURL: 'https://www.googleapis.com/upload/storage/v1/b/poster-ai-bucket/o?uploadType=media&name=app/',
      pushResultsURL: 'http://34.73.42.130:8000/face/',
      files: [],
      uploading: true,
      evaluating: false,
      processing: false,
      hasResults: false,
      evalIndex: 0,
      hasReacted: false,
      stream: null,
      facesPerPoster: {},
      resultsID: 0,
      userCount: 1,
      evaluatingUser: 0,
    };
  },
  computed: {
    uploadSpaceMessage() {
      return 'Upload files here!';
    },
    displayCard() {
      return this.files.length > 0;
    },
    resultsURL() {
      return `/results/${this.resultsID}`;
    }
  },
  methods: {
    startEval() {
      this.uploading = false;
      this.evaluating = true;
      this.evalIndex = 0;

      // Enable webcam
      let video = this.$refs.video;
      if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
          // video.src = window.URL.createObjectURL(stream);
          video.srcObject = stream;
          video.play();
          this.stream = stream;
        });
      }

      // Loop through each poster/image, create an empty array
      for(let file of this.files) {
        this.facesPerPoster[file.id] = [];
      }

    },
    // resetCurrentPoster() {
    //   this.currentPoster['postername'] = this.files[this.evalIndex].file.name;
    //   this.currentPoster['images'] = [];
    // },
    like() {
      // Associate the file with the outcome
      this.files[this.evalIndex].stats = {
        liked: true
      };

      // Move onto next
      this.nextImage();
    },
    dislike() {
      // Associate the file with the outcome
      this.files[this.evalIndex].stats = {
        liked: true
      };

      // Move onto next
      this.nextImage();
    },
    nextImage() {
      // Last image
      if(this.evalIndex >= this.files.length - 1) {

        // Stop evaluation if out of users
        if(this.evaluatingUser >= (this.userCount - 1)) {
          // Stop webcam
          this.stream.getTracks()[0].stop();

          // Change UI state
          this.evaluating = false;
          this.processing = true;

          // Store the images on the cloud
          let imageMap = {};
          let promises = [];
          let uuidToFileID = {};
          for(let file of this.files) {
            imageMap[file.id] = [];


            for(let img of this.facesPerPoster[file.id]) {
              let fn = this.uuid();
              uuidToFileID[`app/${fn}`] = file.id;
              promises.push(axios.post(`${this.uploadImagesURL}${fn}`, this.dataURItoBlob(img), {
                headers: {
                  'Content-Type': 'image/jpeg'
              },}));
            }
          }

          // Handle the face-processing for this image
          axios.all(promises).then(results => {
            // Gather the media links from the results
            results.forEach(response => {
              let fileid = uuidToFileID[response.data.name];
              imageMap[fileid].push(response.data.mediaLink);
              // console.log("Got response");
              // console.log(response);
              // console.log("Media link");
              // console.log(response.data.mediaLink);
            });

            // Use them to construct the request to send to the other API
            let constructed = this.constructForServer(imageMap);
            console.log(constructed);

            // Send to other API, wait for response for these lines
            axios.post(this.pushResultsURL, constructed, {
              headers: {'Content-Type': 'application/json'}
            }).then(response => {
              // Get the session ID
              this.resultsID = response.data.session_id;
              this.processing = false;
              this.hasResults = true;
            }).catch(error => {
              console.log(error.response);
              this.processing = false;
              this.hasResults = false;
            });

            // this.resultsID = 0;

            // console.log("Constructing...");
            // console.log(constructed);
          });

        }
        // Otherwise, we'll reset back to the beginning
        else {
          this.evaluatingUser += 1;
          this.evalIndex = 0;
          this.hasReacted = false;
        }

      } 
      // Continue to next image for evaluation
      else {
        this.evalIndex += 1;
        this.hasReacted = false;
      }
    },
    uuid() {
      return uuidv1();
    },
    /**
     * Captures the current webcam image, saves it to a canvas, and saves the
     * image to an array that'll be passed to the server. 
     */
    capture() {
      this.$refs.canvas.getContext("2d").drawImage(this.$refs.video,0,0,640,480);
      this.hasReacted = true;

      // Capture the image, associate it with the poster/product
      this.facesPerPoster[this.files[this.evalIndex].id].push(this.$refs.canvas.toDataURL());
      // this.imagesArray.push(this.$refs.canvas.toDataURL());
    },
    constructForServer(imageMap) {
      let posters = [];
      for(let file of this.files) {
        posters.push({
          'postername': file.file.name,
          'images': imageMap[file.id]
        })
      }

      return {
        'posters': posters
      }
    },
    inputFilter(newFile, oldFile, prevent) {
      if (newFile && !oldFile) {
        if (!/\.(gif|jpg|jpeg|png|webp)$/i.test(newFile.name)) {
          this.alert('Your choice is not a picture');
          return prevent();
        }
      }
      if (newFile && (!oldFile || newFile.file !== oldFile.file)) {
        newFile.url = '';
        let URL = window.URL || window.webkitURL;
        if (URL && URL.createObjectURL) {
          newFile.url = URL.createObjectURL(newFile.file);
        }
      }
    },
    // https://stackoverflow.com/questions/19032406/convert-html5-canvas-into-file-to-be-uploaded
    dataURItoBlob(dataURI) {
      // convert base64/URLEncoded data component to raw binary data held in a string
      let byteString = atob(dataURI.split(',')[1]);

      // separate out the mime component
      let mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

      // write the bytes of the string to an ArrayBuffer
      let ab = new ArrayBuffer(byteString.length);
      let ia = new Uint8Array(ab);
      for (let i = 0; i < byteString.length; i++) {
          ia[i] = byteString.charCodeAt(i);
      }

      //New Code
      return new Blob([ab], {type: mimeString});
    }
  }
}
</script>

<style>
.survey-grid {
  display: grid;
  grid-template-columns: 50% 50%;
}
.file-upload {
  margin-top: 20px;
  width: 90%;
  height: 100px;
}
.upload-space {
  width: 100%;
  height: 100%;
  margin: auto;
  background-color: #d9dfea
}
.upload-space-hover {
  width: 100%;
  height: 100%;
  margin: auto;
  background-color: #aab1be
}
.img-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center
}
.evaluation {

}
.slider-styles {
  max-width: 200px; 
  margin: auto;
  margin-top: 40px;
}

.opacity-transition-enter-active {
  transition: all .3s ease;
}
.opacity-transition-leave-active {
  opacity: 0;
  transition: all .0s ease;
}
.opacity-transition-enter, .opacity-transition-leave-to {
  opacity: 0;
}

.new-survey-enter-active {
  transition: all .3s ease;
}
.new-survey-leave-active {
  opacity: 0;
  transition: all .0s ease;
}
.new-survey-enter, .new-survey-leave-to {
  transform: translateX(10px);
  opacity: 0;
}

.new-image-enter-active {
  transition: all .5s ease;
}
.new-image-leave-active {
  opacity: 0;
  transition: all .0s ease;
}
.new-image-enter, .new-image-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}

.next-enter-active {
  opacity: 0;
  transition: all .5s ease;
}
.next-leave-active {
  opacity: 0;
  transition: all .5s ease;
}
.next-enter, .next-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
