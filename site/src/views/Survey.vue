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
            <v-card>
              <div class="img-container" v-show="displayCard">
                <transition-group name="new-image">
                  <img v-for="(file, i) in files" :key="i" :src="file.url" style="max-height: 90px">
                </transition-group>
              </div>
            </v-card>
          </transition>

          <!-- Controls for continuing -->
          <transition name="new-survey">
            <v-btn id="continue" large v-if="displayCard" @click="startEval">Continue and Enable Webcam</v-btn>
            <v-btn disabled id="disabled">Add Images to Continue</v-btn>
          </transition>
        </div>
      </transition>


      <!-- Evaluation -->
      <transition name="next">
        <div v-if="evaluating" class="evaluation">
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
        <div v-if="!evaluating && !uploading" class="evaluation">
          <div class="headline font-weight-light font-italic">Processing results... Pretty graphs incoming soon!</div>

          <!-- Progress Spinner! -->
          <v-progress-circular indeterminate :size="100" :width="10" />
        </div>
      </transition>

      <transition name="next">
        <div v-if="hasResults" class="evaluation">
          <div class="headline font-weight-light font-italic">Done! Results available!</div>
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

export default {
  name: 'survey',
  components: { FileUpload },
  data() {
    return {
      files: [],
      uploading: true,
      evaluating: false,
      processing: false,
      hasResults: false,
      evalIndex: 0,
      hasReacted: false,
      stream: null,
      imagesArray: [],
      resultsID: 0
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
    },
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
      // Last image, stop evaluation
      if(this.evalIndex >= this.files.length - 1) {
        // Stop webcam
        this.stream.getTracks()[0].stop();

        // Change UI state
        this.evaluating = false;
        this.processing = true;

        // Send results to the server
        // axios.post(``)

        // Get ID with results

        // Redirect to results page
        this.resultsID = 0;
        this.processing = false;
        this.hasResults = true;
      } 
      // Continue to next image for evaluation
      else {
        this.evalIndex += 1;
        this.hasReacted = false;
      }
    },
    /**
     * Captures the current webcam image, saves it to a canvas, and saves the
     * image to an array that'll be passed to the server. 
     */
    capture() {
      this.$refs.canvas.getContext("2d").drawImage(this.$refs.video,0,0,640,480);
      this.hasReacted = true;
      this.imagesArray.push(this.$refs.canvas.toDataURL());
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
