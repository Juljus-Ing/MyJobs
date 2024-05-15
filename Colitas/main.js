var scenes = document.getElementsByClassName('scene');
for (let index = 0; index < scenes.length; index++) {
  var parallaxInstance = new Parallax(scenes[index], {
    relativeInput: true
  });
};

