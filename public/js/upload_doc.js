
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-app.js";


    //import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-analytics.js";
    // TODO: Add SDKs for Firebase products that you want to use
    // https://firebase.google.com/docs/web/setup#available-libraries
  
    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    import { getStorage,ref, uploadBytesResumable } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-storage.js";
   
    const firebaseConfig = {
        apiKey: "AIzaSyBTeb_PvF8zbxl4IbJNuLUBJ59bydYIIX0",
        authDomain: "login-database-a039a.firebaseapp.com",
        databaseURL: "https://login-database-a039a-default-rtdb.firebaseio.com",
        projectId: "login-database-a039a",
        storageBucket: "login-database-a039a.appspot.com",
        messagingSenderId: "244501067021",
        appId: "1:244501067021:web:273b9f3850222581b26c44",
        measurementId: "G-3K356FGCLX",
        storageBucket:"gs://login-database-a039a.appspot.com"
};

        // Initialize Firebase
        const app = initializeApp(firebaseConfig);

// Initialize Firebase Authentication and get a reference to the service
       
        const storage = getStorage();
     
        
        const userCreds = JSON.parse(sessionStorage.getItem("user-creds"));
        const fileInput = document.querySelector("#input-doc");
        // Assuming you have a file input with the id "input-doc"
       let url;
       let docUpload=evt =>{    
        evt.preventDefault(); 
        // Check if a file is selected
        if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const name = file.name;
        const metadata = {
            contentType: file.type,
        };

        // Create a storage reference for the file in the user's Documents folder
        const storageRef = ref(storage, `${userCreds.uid}/${name}`);

        // Upload the file with metadata
        const uploadTask = uploadBytesResumable(storageRef, file, metadata);
      
        
        // Set up observers to monitor the upload task
        uploadTask.on( 'state_changed',
             (snapshot) => {
            // Handle upload progress
            const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
            console.log(`Upload is ${progress}% done`);
            }, 
            (error) => {
            // Handle unsuccessful uploads
            console.error('Error during upload:', error);
            }, 
            () => {
            // Handle successful upload
            console.log('File uploaded successfully');

            //Optionally, you can get the download URL
            
        }
        );
        } else {
        console.error('No file selected');
        }
    }
    const submitButton = document.getElementById("next");
    submitButton.addEventListener("click", docUpload);
    
    

    
    