const logNav = document.querySelector(".log-nav");
const profile = document.querySelector(".account");
var flag = 0;
profile.addEventListener("mouseenter",()=>{
    if(flag==0){
        logNav.style.display = "flex";
        flag = 1;
    }else{
        profile.addEventListener("mouseleave",()=>{
            logNav.style.display = "none";
            flag = 0;
        })
    }
})
profile.addEventListener("mouseleave",()=>{
    logNav.style.display = "none";
})
var typed = new Typed(".welcome-effect",{
    strings:["track your expenses now !!"],
    typeSpeed:90,
    backSpeed:90,
    backDelay:1250,
    startDelay:500,
    cursorChar:"!",
    loop:true
});
