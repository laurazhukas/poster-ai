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
            <v-btn id="continue" large v-if="displayCard" @click="startEval">Continue</v-btn>
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
          <v-btn @click="startReaction" :disabled="reacting">Capture Reaction</v-btn>
          <v-btn @click="capture">Cap</v-btn>

          <!-- Like/dislike -->
          <div>
            <v-btn color="error" @click="dislike" :disabled="!hasReacted">Dislike</v-btn>
            <v-btn color="success" @click="like" :disabled="!hasReacted">Like</v-btn>
          </div>

        </div>
      </transition>

      <video v-show="false" ref="video" id="video" width="640" height="480" autoplay></video>
      <canvas ref="canvas" id="canvas" width="640" height="480"/>
      
    </div>
  </transition>
</template>

<script>
import FileUpload from 'vue-upload-component';

export default {
  name: 'survey',
  components: { FileUpload },
  data() {
    return {
      files: [],
      uploading: true,
      evaluating: false,
      confirmation: false,
      evalIndex: 0,
      hasReacted: false,
      reacting: false
    };
  },
  computed: {
    uploadSpaceMessage() {
      return 'Upload files here!';
    },
    displayCard() {
      return this.files.length > 0;
    }
  },
  methods: {
    startEval() {
      this.uploading = false;
      this.evaluating = true;
      this.evalIndex = 0;
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
      // Check for remaining files
      if(this.evalIndex >= this.files.length - 1) {
        this.evaluating = false;
        this.confirmation = true;
        this.hasReacted = false;
      } else {
        this.evalIndex += 1;
      }
    },
    startReaction() {
      this.reacting = true;

      let video = this.$refs.video;
      if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
          // video.src = window.URL.createObjectURL(stream);
          video.srcObject = stream;
          video.play();

          // For capturing the reaction
          // function capture(context, video) {
          //   // let canvas = this.$refs.canvas;
          //   // let context = canvas.getContext("2d").drawImage(video, 0, 0, 640, 480);
          //   context.drawImage(video, 0, 0, 640, 480);

          // }
        });
        
      }
    },
    capture() {
      this.$refs.canvas.getContext("2d").drawImage(this.$refs.video,
      0,0,640,480);
    },
    // capture(context, video) {
    //   // let canvas = this.$refs.canvas;
    //   // let context = canvas.getContext("2d").drawImage(video, 0, 0, 640, 480);
    //   console.log("Capturing...");
    //   context.drawImage(video, 0, 0, 640, 480);
    //   // video.stop();
    //   this.endReaction();
    // },
    endReaction() {
      this.reacting = false;
      this.hasReacted = true;
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
  width: 100%;
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
