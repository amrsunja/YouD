async function download_video(){
    var link_video = document.getElementById('video_down').value;
    await eel.download_video(link_video)();
    
}

async function download_audio(){
    var link_audio = document.getElementById('audio_down').value;
    await eel.download_audio(link_audio)();
}
