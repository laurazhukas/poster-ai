<template>
  <div class="page-style">
    <!-- Title -->
    <div class="font-weight-medium display-3">Survey Results</div>

    <!-- Display things in a grid -->
    <div class="page-grid">
      <!-- Raw numbers overview -->
      <div class="numbers-overview">
        <div class="font-weight-bold headline" style="text-align: center">Basic Stats</div>
        <v-divider/>
        <div class="font-weight-light headline"><span class="font-weight-bold">{{postersCount}}</span> {{posterMsg}}</div>
        <div class="font-weight-light headline"><span class="font-weight-bold">{{usersCount}}</span> {{usersMsg}}</div>
        <div class="font-weight-light headline"><span class="font-weight-bold">{{totalProcessed}}</span> {{totalMsg}}</div>
        <div class="font-weight-light headline">{{targetMsg}} : <span class="font-weight-bold">{{targetEmotion}}</span></div>
      </div>


      <div class="avg-emotions"> <!-- Average emotions graph -->
        <div class="font-weight-bold headline">Average Emotions per Image</div>
        <v-divider/>
        <avg-emot class="graph-style" :data="processedData" :emotions="chosenEmotions"/>
        <div class="font-weight-light title">Choose Emotions to Compare</div>
        <v-combobox class="graph-style"
          v-model="chosenEmotions" :items="possibleEmotions"
          multiple chips/>
      </div>
      
      <div> <!-- User age graph -->
        <div class="font-weight-bold headline" style="text-align: center">User Age Demographic</div>
        <v-divider/>
        <user-age/>
      </div>

      <div> <!-- User radar graph -->
        <div class="font-weight-bold headline" style="text-align: center">All User Emotions</div>
        <v-divider/>
         <radar/>
         <br>
      </div>
    </div>
  </div>
</template>

<script>
import AvgEmot from '../components/GAverageEmotion';
import UserAge from '../components/userAgeDemographic.vue';
import radar from '../components/radarGraph.vue';

export default {
  components: { AvgEmot, UserAge, radar },
  mounted() {
    // Load stuff

    // Process the data
    let posterMap = {};
    let posterIDs = [];

    for(let beforeFace of this.beforeProcessed) {
      // Sort by poster_id
      if(posterMap[beforeFace.poster_id] == null) {
        posterIDs.push(beforeFace.poster_id);
        posterMap[beforeFace.poster_id] = {
          id: beforeFace.poster_id,
          name: beforeFace.poster_name,
          faces: []
        };
      }
      posterMap[beforeFace.poster_id].faces.push(beforeFace);
    }

    for(let id of posterIDs) {
      this.processedData.push(posterMap[id]);
    }



    console.log(this.processedData);

    // Pre-load the graph according to the target emotion
    this.chosenEmotions.push(this.targetEmotion.toLowerCase());
  },
  data() {
    return {
      beforeProcessed: [
        {
            "url": "http://127.0.0.1:8000/face/4/",
            "face_id": "4e7b50b0-4cc7-4e72-a2ad-221e5dac3a07",
            "gender": "male",
            "age": 29,
            "anger": "0",
            "contempt": "0",
            "disgust": "0",
            "fear": "0",
            "happiness": "0",
            "neutral": "1",
            "sadness": "0",
            "surprise": "0",
            "poster_id": "8d99c923-570d-4991-aea6-b09c09fe3a86",
            "session_id": "4314ac74-2070-4712-afda-01ffd70dec17",
            "image_uri": "https://storage.googleapis.com/poster-ai-bucket/aberdeen-faces-dataset/andrew!45.jpg",
            "poster_name": "blob1"
        },
        {
          "url": "http://127.0.0.1:8000/face/4/",
          "face_id": "4e7b50b0-4cc7-4e72-a2ad-221e5dac3a07",
          "gender": "male",
          "age": 29,
          "anger": "0.5",
          "contempt": "0.2",
          "disgust": "0",
          "fear": "0",
          "happiness": "0",
          "neutral": "0.1",
          "sadness": "0.2",
          "surprise": "0",
          "poster_id": "8d99c923-570d-4991-aea6-b09c09fe3a86",
          "session_id": "4314ac74-2070-4712-afda-01ffd70dec17",
          "image_uri": "https://storage.googleapis.com/poster-ai-bucket/aberdeen-faces-dataset/andrew!45.jpg",
          "poster_name": "blob1"
        },
        {
          "url": "http://127.0.0.1:8000/face/4/",
          "face_id": "4e7b50b0-4cc7-4e72-a2ad-221e5dac3a07",
          "gender": "male",
          "age": 29,
          "anger": "0.5",
          "contempt": "0.2",
          "disgust": "0.000000000000",
          "fear": "0.000000000000",
          "happiness": "0.000000000000",
          "neutral": "0.1",
          "sadness": "0.2",
          "surprise": "0.000000000000",
          "poster_id": "8d99c923-570d-4991-aea6-b09c09fe3123",
          "session_id": "4314ac74-2070-4712-afda-01ffd70dec17",
          "image_uri": "https://storage.googleapis.com/poster-ai-bucket/aberdeen-faces-dataset/andrew!45.jpg",
          "poster_name": "blob2"
        },
        {
          "url": "http://127.0.0.1:8000/face/4/",
          "face_id": "4e7b50b0-4cc7-4e72-a2ad-221e5dac3a07",
          "gender": "male",
          "age": 29,
          "anger": "0.0",
          "contempt": "0.2",
          "disgust": "0.000000000000",
          "fear": "0.000000000000",
          "happiness": "0.5",
          "neutral": "0.1",
          "sadness": "0.2",
          "surprise": "0.000000000000",
          "poster_id": "8d99c923-570d-4991-aea6-b09c09fe3123",
          "session_id": "4314ac74-2070-4712-afda-01ffd70dec17",
          "image_uri": "https://storage.googleapis.com/poster-ai-bucket/aberdeen-faces-dataset/andrew!45.jpg",
          "poster_name": "blob2"
        }
      ],
      mockData: [
        {
          id: "Poster_A",
          faces: [
            {
              faceAttributes: {
                emotions: {
                  "anger": 0, "contempt": 0,
                  "disgust": 0, "fear": 0,
                  "happiness": 0, "neutral": 0.5,
                  "sadness": 0, "surprise": 0
                }
              }
            },
            {
              faceAttributes: {
                emotions: {
                  "anger": 0, "contempt": 0.1,
                  "disgust": 0, "fear": 0,
                  "happiness": 0.5, "neutral": 0.0,
                  "sadness": 0, "surprise": 0.2
                }
              }
            },
            {
              faceAttributes: {
                emotions: {
                  "anger": 0, "contempt": 0.0,
                  "disgust": 0, "fear": 0,
                  "happiness": 0.9, "neutral": 0.0,
                  "sadness": 0, "surprise": 0.5
                }
              }
            },
            {
              faceAttributes: {
                emotions: {
                  "anger": 0.3, "contempt": 0.5,
                  "disgust": 0, "fear": 0,
                  "happiness": 0.1, "neutral": 0.2,
                  "sadness": 0, "surprise": 0.2
                }
              }
            },
          ]
        },
        {
          id: "Poster_B",
          faces: [
            {
              faceAttributes: {
                emotions: {
                  "anger": 0, "contempt": 0,
                  "disgust": 0, "fear": 0,
                  "happiness": 0, "neutral": 0.2,
                  "sadness": 0, "surprise": 0.3
                }
              }
            },
            {
              faceAttributes: {
                emotions: {
                  "anger": 0, "contempt": 0.1,
                  "disgust": 0, "fear": 0,
                  "happiness": 0.9, "neutral": 0.0,
                  "sadness": 0, "surprise": 0.2
                }
              }
            },
            {
              faceAttributes: {
                emotions: {
                  "anger": 0, "contempt": 0.0,
                  "disgust": 0, "fear": 0.4,
                  "happiness": 0.3, "neutral": 0.0,
                  "sadness": 0, "surprise": 0.5
                }
              }
            },
            {
              faceAttributes: {
                emotions: {
                  "anger": 0.3, "contempt": 0.5,
                  "disgust": 0, "fear": 0.9,
                  "happiness": 0.1, "neutral": 0.2,
                  "sadness": 0, "surprise": 0.2
                }
              }
            },
          ]
        },

      ],
      processedData: [],
      emotions: {
        'Anger': {key: 'anger', color: '#ffffff'},
        'Contempt': {key: 'contempt', color: '#ffffff'},
        'Disgust': {key: 'disgust', color: '#ffffff'},
        'Fear': {key: 'fear', color: '#ffffff'},
        'Happiness': {key: 'happiness', color: '#ffffff'},
        'Neutral': {key: 'neutral', color: '#ffffff'},
        'Sadness': {key: 'sadness', color: '#ffffff'},
        'Surprise': {key: 'surprise', color: '#ffffff'},
      },
      chosenEmotions: [],
      possibleEmotions: [
        'anger',
        'contempt',
        'disgust',
        'fear',
        'happiness',
        'neutral',
        'sadness',
        'surprise'
      ],
      postersCount: 5,
      usersCount: 5,
      targetEmotion: 'Happiness'
    };
  },
  computed: {
    posterMsg() {
      return `Posters Evaluated`;
    },
    usersMsg() {
      return `Users Provided Feedback`;
    },
    totalMsg() {
      return `Total Images Processed`
    },
    targetMsg() {
      return `Target Emotion`;
    },
    totalProcessed() {
      return `${this.postersCount * this.usersCount}`;
    }
  }
}
</script>

<style>
.graph-style {
  max-height: 400px;
  max-width: 500px;
  margin: auto;
  margin-bottom: 20px;
}
.page-style {
  text-align: center;
  margin-left: 10%;
  margin-right: 10%;
}
.page-grid {
  display: grid;
  grid-template-columns: 50% 50%;
}
.numbers-overview {
  text-align: left;
}
@media only screen and (max-width: 729px) {
  .page-style {
    text-align: center;
    margin-left: 20px;
    margin-right: 20px;
  }
  .page-grid {
    display: grid;
    grid-template-columns: 100%;
  }
  .numbers-overview {
    text-align: center;
  }
}
</style>
