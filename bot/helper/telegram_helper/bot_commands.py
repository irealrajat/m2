from ...core.config_manager import Config


class BotCommands:
    StartCommand = f"start{Config.CMD_SUFFIX}"
    MirrorCommand = [f"mirrorz{Config.CMD_SUFFIX}", f"m2{Config.CMD_SUFFIX}"]
    QbMirrorCommand = [f"qbmirrorz{Config.CMD_SUFFIX}", f"qm2{Config.CMD_SUFFIX}"]
    JdMirrorCommand = [f"jdmirror{Config.CMD_SUFFIX}", f"jm{Config.CMD_SUFFIX}"]
    YtdlCommand = [f"ytdlz{Config.CMD_SUFFIX}", f"y2{Config.CMD_SUFFIX}"]
    NzbMirrorCommand = [f"nzbmirrorz{Config.CMD_SUFFIX}", f"nm{Config.CMD_SUFFIX}"]
    LeechCommand = [f"leechz{Config.CMD_SUFFIX}", f"l2{Config.CMD_SUFFIX}"]
    QbLeechCommand = [f"qbleechz{Config.CMD_SUFFIX}", f"ql2{Config.CMD_SUFFIX}"]
    JdLeechCommand = [f"jdleech{Config.CMD_SUFFIX}", f"jl{Config.CMD_SUFFIX}"]
    YtdlLeechCommand = [f"ytdlleechz{Config.CMD_SUFFIX}", f"yl2{Config.CMD_SUFFIX}"]
    NzbLeechCommand = [f"nzbleechz{Config.CMD_SUFFIX}", f"nl2{Config.CMD_SUFFIX}"]
    CloneCommand = f"clonez{Config.CMD_SUFFIX}"
    CountCommand = f"countz{Config.CMD_SUFFIX}"
    DeleteCommand = f"delz{Config.CMD_SUFFIX}"
    CancelTaskCommand = [f"cancelz{Config.CMD_SUFFIX}", f"c2{Config.CMD_SUFFIX}"]
    CancelAllCommand = f"cancelallz{Config.CMD_SUFFIX}"
    ForceStartCommand = [f"forcestartz{Config.CMD_SUFFIX}", f"fs2{Config.CMD_SUFFIX}"]
    ListCommand = f"listz{Config.CMD_SUFFIX}"
    SearchCommand = f"searchz{Config.CMD_SUFFIX}"
    StatusCommand = f"statusz{Config.CMD_SUFFIX}"
    UsersCommand = f"usersz{Config.CMD_SUFFIX}"
    AuthorizeCommand = f"authz{Config.CMD_SUFFIX}"
    UnAuthorizeCommand = f"unauthz{Config.CMD_SUFFIX}"
    AddSudoCommand = f"addsudoz{Config.CMD_SUFFIX}"
    RmSudoCommand = f"rmsudoz{Config.CMD_SUFFIX}"
    PingCommand = f"pingz{Config.CMD_SUFFIX}"
    RestartCommand = f"restartz{Config.CMD_SUFFIX}"
    RestartSessionsCommand = f"restartses{Config.CMD_SUFFIX}"
    StatsCommand = f"statsz{Config.CMD_SUFFIX}"
    HelpCommand = f"helpz{Config.CMD_SUFFIX}"
    LogCommand = f"logz{Config.CMD_SUFFIX}"
    ShellCommand = f"shellz{Config.CMD_SUFFIX}"
    AExecCommand = f"aexecz{Config.CMD_SUFFIX}"
    ExecCommand = f"execz{Config.CMD_SUFFIX}"
    ClearLocalsCommand = f"clearlocalsz{Config.CMD_SUFFIX}"
    BotSetCommand = [f"bsettingz{Config.CMD_SUFFIX}", f"bs2{Config.CMD_SUFFIX}"]
    UserSetCommand = [f"usettingz{Config.CMD_SUFFIX}", f"us2{Config.CMD_SUFFIX}"]
    SelectCommand = f"selz{Config.CMD_SUFFIX}"
    RssCommand = f"rssz{Config.CMD_SUFFIX}"
