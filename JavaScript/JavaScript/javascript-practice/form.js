const registrationForm = document.getElementById("registrationForm");

let fname = registrationForm.querySelector("#fname");
let lname = registrationForm.querySelector("#lname");
let email = registrationForm.querySelector("#email");
let phone = registrationForm.querySelector("#phone");
let password = registrationForm.querySelector("#password");
let dob = registrationForm.querySelector("#dob");
let gender = registrationForm.querySelector("[name='gender']:checked");
let country = registrationForm.querySelector("#country");
let city = registrationForm.querySelector("#city");


registrationForm?.addEventListener("submit", function (e) {

    e.preventDefault();

    let fnameValue = fname?.value?.trim();
    let lnameValue = lname?.value?.trim();
    let passwordValue = password?.value?.trim();
    let emailValue = email?.value?.trim();
    let phoneValue = phone?.value?.trim();
    let dobValue = dob?.value;

    let gender = registrationForm.querySelector("[name='gender']:checked");
    let genderValue = gender?.value?.trim();

    let countryValue = country?.value?.trim();
    let cityValue = city?.value?.trim();

    let skills = registrationForm.querySelectorAll("[name='skills']:checked");

    let skillsValue = [];

    skills.forEach(function (skill) {
        skillsValue.push(skill.value);
    });

    let fnameError = false;
    let lnameError = false;
    let emailError = false;
    let phoneError = false;
    let passwordError = false;
    let dobError = false;
    let genderError = false;
    let countryError = false;
    let cityError = false;
    let skillsError = false;

    if (!fname || !checkfName(fnameValue, fname)) {
        fnameError = true;
    }

    if (!lname || !checklName(lnameValue, lname)) {
        lnameError = true;
    }

    if (!email || !checkEmail(emailValue, email)) {
        emailError = true;
    }

    if (!phone || !checkPhone(phoneValue, phone)) {
        phoneError = true;
    }

    if (!password || !checkPassword(passwordValue, password)) {
        passwordError = true;
    }

    if (!dob || !checkDob(dobValue, dob)) {
        dobError = true;
    }

    if (!checkGender(genderValue)) {
        genderError = true;
    }

    if (!country || !checkCountry(countryValue, country)) {
        countryError = true;
    }

    if (!city || !checkCity(cityValue, city)) {
        cityError = true;
    }

    if (!checkSkills(skillsValue)) {
        skillsError = true;
    }



    if (
        !fnameError &&
        !lnameError &&
        !emailError &&
        !phoneError &&
        !passwordError &&
        !dobError &&
        !genderError &&
        !countryError &&
        !cityError &&
        !skillsError
    ) {

        console.log("no Error found. The form can be submitted now");

        console.log("First Name:", fnameValue);
        console.log("Last Name:", lnameValue);
        console.log("Email:", emailValue);
        console.log("Phone:", phoneValue);
        console.log("Password:", passwordValue);
        console.log("DOB:", dobValue);
        console.log("Gender:", genderValue);
        console.log("Country:", countryValue);
        console.log("City:", cityValue);
        console.log("Skills:", skillsValue);

    } else {

        console.log("Please fill the form correctly and submit again");

    }

});

function checkfName(fname, el) {

    let passed = true;

    let pattern = /^(?=.{3,100}$)[\p{L}]+(?:[ '-][\p{L}]+)*$/u;

    passed = pattern.test(fname);

    let errorel = el?.closest("form")?.querySelector(".fname-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checklName(lname, el) {

    let passed = true;

    let pattern = /^(?=.{0,100}$)[\p{L}]+(?:[ '-][\p{L}]+)*$/u;

    passed = pattern.test(lname);

    let errorel = el?.closest("form")?.querySelector(".lname-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checkEmail(email, el) {

    let passed = true;

    let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    passed = pattern.test(email);

    let errorel = el?.closest("form")?.querySelector(".email-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checkPhone(phone, el) {

    let passed = true;

    let pattern = /^[6-9]\d{9}$/;

    passed = pattern.test(phone);

    let errorel = el?.closest("form")?.querySelector(".phone-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checkPassword(password, el) {

    let passed = true;

    let pattern =
        /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/;

    passed = pattern.test(password);

    let errorel = el?.closest("form")?.querySelector(".password-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checkDob(dob, el) {

    let passed = true;

    passed = dob !== "";

    let errorel = el?.closest("form")?.querySelector(".dob-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checkGender(gender) {

    let passed = true;

    passed = !!gender;

    let errorel = registrationForm.querySelector(".gender-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checkCountry(country, el) {

    let passed = true;

    passed = country !== "";

    let errorel = el?.closest("form")?.querySelector(".country-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}

function checkCity(city, el) {

    let passed = true;

    let pattern = /^(?=.{3,100}$)[\p{L}]+(?:[ '-][\p{L}]+)*$/u;

    passed = pattern.test(city);

    let errorel = el?.closest("form")?.querySelector(".city-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


function checkSkills(skills) {

    let passed = true;

    passed = skills.length > 0;

    let errorel = registrationForm.querySelector(".skills-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


fname?.addEventListener("change", function () {
    checkfName(fname.value?.trim(), fname);
});


lname?.addEventListener("change", function () {
    checklName(lname.value?.trim(), lname);
});

email?.addEventListener("change", function () {
    checkEmail(email.value?.trim(), email);
});

phone?.addEventListener("change", function () {
    checkPhone(phone.value?.trim(), phone);
});


password?.addEventListener("change", function () {
    checkPassword(password.value?.trim(), password);
});

dob?.addEventListener("change", function () {
    checkDob(dob.value, dob);
});

country?.addEventListener("change", function () {
    checkCountry(country.value?.trim(), country);
});


city?.addEventListener("change", function () {
    checkCity(city.value?.trim(), city);
});

registrationForm
    .querySelectorAll("[name='gender']")
    .forEach(function (genderInput) {

        genderInput.addEventListener("change", function () {

            let gender = registrationForm.querySelector(
                "[name='gender']:checked"
            );

            checkGender(gender?.value);

        });

    });

registrationForm
    .querySelectorAll("[name='skills']")
    .forEach(function (skillInput) {

        skillInput.addEventListener("change", function () {

            let skills = registrationForm.querySelectorAll(
                "[name='skills']:checked"
            );

            let skillsValue = [];

            skills.forEach(function (skill) {
                skillsValue.push(skill.value);
            });

            checkSkills(skillsValue);

        });

    });