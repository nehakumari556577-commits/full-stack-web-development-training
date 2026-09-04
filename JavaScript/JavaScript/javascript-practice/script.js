const users = [
    {
        id: 101,
        name: " alex JOHNSON ",
        dob: "1992-06-15",
        salary: "55000",
        skills: ["html", "css", "javascript"]
    },
    {
        id: 102,
        name: " maria smith ",
        dob: "1988-11-03",
        salary: "72000",
        skills: ["react", "node", "css"]
    },
    {
        id: 103,
        name: "john doe",
        dob: "1996-02-25",
        salary: "48000",
        skills: ["vue", "javascript", "html"]
    }
];


function titleCase(str) {
    return str
        .trim()
        .toLowerCase()
        .split(" ")
        .filter(word => word)
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");
}


function formatDate(date) {
    return new Date(date).toLocaleDateString("en-GB", {
        day: "2-digit",
        month: "short",
        year: "numeric"
    });
}


function calculateAge(dob) {
    const birth = new Date(dob);
    const today = new Date();

    let age = today.getFullYear() - birth.getFullYear();

    const month = today.getMonth() - birth.getMonth();

    if (month < 0 || (month === 0 && today.getDate() < birth.getDate())) {
        age--;
    }

    return age;
}


function formatSkills(skills) {
    return skills
        .map(skill => skill.charAt(0).toUpperCase() + skill.slice(1))
        .join(", ");
}

function renderTable() {

    const tbody = document.querySelector("#userTable tbody");

    tbody.innerHTML = "";

    users.forEach((user, index) => {

        const row = `
        <tr>
            <td>${titleCase(user.name)}</td>
            <td>${formatDate(user.dob)}</td>
            <td>${calculateAge(user.dob)}</td>
            <td>${Number(user.salary)}</td>
            <td>${formatSkills(user.skills)}</td>
            <td>
                <button class="delete-btn" onclick="deleteUser(${index})">Delete</button>
                <button class="edit-btn" onclick="editUser(${index})">Edit</button>
            </td>
        </tr>
        `;

        tbody.innerHTML += row;

    });

}

renderTable();

function deleteUser(index) {
    users.splice(index, 1);
    renderTable();
}

function editUser(index) {

    const user = users[index];

    document.getElementById("modal").style.display = "block";

    document.getElementById("userIndex").value = index;

    document.getElementById("name").value = user.name.trim();
    document.getElementById("dob").value = user.dob;
    document.getElementById("salary").value = user.salary;
    document.getElementById("skills").value = user.skills.join(", ");

}


function closeModal() {
    document.getElementById("modal").style.display = "none";
}


document.getElementById("editForm").addEventListener("submit", function (e) {

    e.preventDefault();

    const index = document.getElementById("userIndex").value;

    users[index].name = document.getElementById("name").value;
    users[index].dob = document.getElementById("dob").value;
    users[index].salary = document.getElementById("salary").value;
    users[index].skills = document
        .getElementById("skills")
        .value
        .split(",")
        .map(skill => skill.trim());

    closeModal();
    renderTable();

});


// const registrationForm = document.getElementById("registrationForm");
// let fname = registrationForm.querySelector("#fname")
// let lname = registrationForm.querySelector("#lname")
// let email = registrationForm.querySelector("#email")
// let phone = registrationForm.querySelector("#phone")
// let password = registrationForm.querySelector("#password")
// let dob = registrationForm.querySelector("#dob")
// let gender = registrationForm.querySelector("[name='gender']:checked")
// let country = registrationForm.querySelector("#country")
// let city = registrationForm.querySelector("#city")

// registrationForm?.addEventListener("submit", function(e){
//     e.preventDefault(); 

//     let fnameValue = fname?.value?.trim()
//     let lnameValue = lname?.value?.trim()
//     let passwordValue = password?.value?.trim()
//     let emailValue = email?.value?.trim()
//     let phoneValue = phone?.value?.trim()
//     let dobValue = dob?.value
//     let genderValue = gender?.value?.trim()
//     let countryValue = country?.value?.trim()
//     let cityValue = city?.value?.trim()
//     let fnameError = false;
//     let lnameError = false;
//     let emailError = false;
//     let phoneError = false;
//     let passwordError = false;
//     let dobError = false;
//     let genderError = false;
//     let countryError = false;
//     let cityError = false;

//     if(!fname || !checkfName(fnameValue, fname)){
//         fnameError = true;        
//     }
//     if(!lname || !checklName(lnameValue, lname)){
//         lnameError = true;        
//     }
//     if(!email || !checkEmail(emailValue, email)){
//         emailError = true;        
//     }
//     if(!phone || !checkPhone(phoneValue, phone)){
//         phoneError = true;        
//     }
//     if(!password || !checkPassword(passwordValue, password)){
//         passwordError = true;        
//     }


//     if(!fnameError && !lnameError && !emailError && !phoneError && !passwordError && !dobError && !genderError && !countryError && !cityError){
//         console.log('no Error found. The form can be submitted now')
//     }else{
//         console.log('Please fill the form correctly and submit again')
//     }
    
    

// });


// function checkfName(fname, el){
//     let passed = true;
//     let pattern = /^(?=.{3,100}$)[\p{L}]+(?:[ '-][\p{L}]+)*$/u
//     passed = pattern.test(fname)
//     let errorel = el?.closest("form")?.querySelector(".fname-error");
//     if(!passed){
//        errorel?.classList.add("show")
//     }else{
//         errorel?.classList.remove("show")

//     }
//     return passed
// }
// function checklName(lname, el){
//     let passed = true;
//     let pattern = /^(?=.{0,100}$)[\p{L}]+(?:[ '-][\p{L}]+)*$/u
//     passed = pattern.test(lname)
//     let errorel = el?.closest("form")?.querySelector(".lname-error");
//     if(!passed){
//        errorel?.classList.add("show")
//     }else{
//         errorel?.classList.remove("show")

//     }
//     return passed
// }
// function checkEmail(email, el){
//     let passed = true;
//     let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
//     passed = pattern.test(email)
//     let errorel = el?.closest("form")?.querySelector(".email-error");
//     if(!passed){
//        errorel?.classList.add("show")
//     }else{
//         errorel?.classList.remove("show")

//     }
//     return passed
// }
// function checkPhone(phone, el){
//     let passed = true;
//     let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
//     passed = pattern.test(phone)
//     let errorel = el?.closest("form")?.querySelector(".phone-error");
//     if(!passed){
//        errorel?.classList.add("show")
//     }else{
//         errorel?.classList.remove("show")

//     }
//     return passed
// }
// function checkPassword(password, el){
//     let passed = true;
//     let pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/
//     passed = pattern.test(password)
//     let errorel = el?.closest("form")?.querySelector(".password-error");
//     if(!passed){
//        errorel?.classList.add("show")
//     }else{
//         errorel?.classList.remove("show")
//     }
//     return passed
// }

// // const fnameEl = registrationForm.querySelector

// fname?.addEventListener("change", function(){
//     checkfName(fname.value?.trim(), fname);
// });