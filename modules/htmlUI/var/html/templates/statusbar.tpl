{include file="script/clock.js.tpl"}
<div id="statusbar">

    <div class="statusbaritem">
        server time
        <br>
        <span id=servertime style="position:relative;"></span>
    </div>

    <div class="statusbaritem">
        local  time
        <br>
        <span id=localtime style="position:relative;"></span>
    </div>

    <div class="statusbaritem">
        <img src="{$systemPrefs.stationLogoPath}" width="30" height="50">
    </div>

    <div class="statusbaritem">
        {$systemPrefs.stationName}
        <br>
        {$systemPrefs.frequency}
    </div>

    <div class="statusbaritem">
        {include file="userinfo.tpl"}
    </div>

</div>
