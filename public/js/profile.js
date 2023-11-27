import { initializeApp } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-app.js";
   
    //import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-analytics.js";
    // TODO: Add SDKs for Firebase products that you want to use
    // https://firebase.google.com/docs/web/setup#available-libraries
  
    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    import { getStorage,ref,  listAll, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-storage.js";
    import { getAuth,signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-auth.js";
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
        
        document.addEventListener("DOMContentLoaded", () => {
            const userInfo = JSON.parse(sessionStorage.getItem("user-info"));
            console.log("userInfo",userInfo.fullName);
            document.getElementById("display").innerHTML = userInfo.fullName;
    
        });
      
        const userCreds = JSON.parse(sessionStorage.getItem("user-creds"));
        // Reference to the root of your storage bucket
        const storageRef = ref(storage, `${userCreds.uid}/`); // Replace '/' with your desired path

// List all items at the root
        listAll(storageRef)
        .then((result) => {
            result.items.forEach((itemRef) => {
            // Access each file using itemRef
            getDownloadURL(itemRef)
                .then((url) => {

                    var a = document.createElement('a');
                    const fileRef = ref(storage, url);

                    const fileName = fileRef.name;
                    var linkText = document.createTextNode(`${fileName}`);
                    a.appendChild(linkText);
                    a.title = "my title text";
                    a.href = url;
                    a.style.display = "block";
                    document.getElementById("files").insertAdjacentElement('afterend',a);
                   // document.body.appendChild(a);
                console.log('File URL:', url);
                
            })
                .catch((error) => {
                console.error('Error getting download URL:', error);
                });
            });
        })
        .catch((error) => {
            console.error('Error listing items:', error);
        });


