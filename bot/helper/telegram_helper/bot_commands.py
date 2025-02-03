from ...core.config_manager import Config


class _BotCommands:
    def __init__(self):
        self.StartCommand = f"start{Config.CMD_SUFFIX}"
        self.MirrorCommand = [f"mirrorz{Config.CMD_SUFFIX}", f"m2{Config.CMD_SUFFIX}"]
        self.QbMirrorCommand = [f"qbmirrorz{Config.CMD_SUFFIX}", f"qm2{Config.CMD_SUFFIX}"]
        self.JdMirrorCommand = [f"jdmirror{Config.CMD_SUFFIX}", f"jm{Config.CMD_SUFFIX}"]
        self.YtdlCommand = [f"ytdlz{Config.CMD_SUFFIX}", f"y2{Config.CMD_SUFFIX}"]
        self.NzbMirrorCommand = [f"nzbmirror{Config.CMD_SUFFIX}", f"nm{Config.CMD_SUFFIX}"]
        self.LeechCommand = [f"leechz{Config.CMD_SUFFIX}", f"l2{Config.CMD_SUFFIX}"]
        self.QbLeechCommand = [f"qbleechz{Config.CMD_SUFFIX}", f"ql2{Config.CMD_SUFFIX}"]
        self.JdLeechCommand = [f"jdLeech{Config.CMD_SUFFIX}", f"jl{Config.CMD_SUFFIX}"]
        self.YtdlLeechCommand = [f"ytdlleechz{Config.CMD_SUFFIX}", f"yl2{Config.CMD_SUFFIX}"]
        self.NzbLeechCommand = [f"nzbleech{Config.CMD_SUFFIX}", f"nl{Config.CMD_SUFFIX}"]
        self.CloneCommand = f"clonez{Config.CMD_SUFFIX}"
        self.CountCommand = f"countz{Config.CMD_SUFFIX}"
        self.DeleteCommand = f"delz{Config.CMD_SUFFIX}"
        self.CancelTaskCommand = [f"cancelz{Config.CMD_SUFFIX}", f"c2{Config.CMD_SUFFIX}"]
        self.CancelAllCommand = f"cancelallz{Config.CMD_SUFFIX}"
        self.ForceStartCommand = [f"forcestart{Config.CMD_SUFFIX}", f"fs{Config.CMD_SUFFIX}"]
        self.ListCommand = f"listz{Config.CMD_SUFFIX}"
        self.SearchCommand = f"searchz{Config.CMD_SUFFIX}"
        self.StatusCommand = f"statusz{Config.CMD_SUFFIX}"
        self.UsersCommand = f"users{Config.CMD_SUFFIX}"
        self.AuthorizeCommand = f"authorizez{Config.CMD_SUFFIX}"
        self.UnAuthorizeCommand = f"unauthorizez{Config.CMD_SUFFIX}"
        self.AddSudoCommand = f"addsudo{Config.CMD_SUFFIX}"
        self.RmSudoCommand = f"rmsudo{Config.CMD_SUFFIX}"
        self.PingCommand = f"pingz{Config.CMD_SUFFIX}"
        self.RestartCommand = f"restartz{Config.CMD_SUFFIX}"
        self.RestartSessionsCommand = f"restartses{Config.CMD_SUFFIX}"
        self.StatsCommand = f"statsz{Config.CMD_SUFFIX}"
        self.HelpCommand = f"help{Config.CMD_SUFFIX}"
        self.LogCommand = f"logz{Config.CMD_SUFFIX}"
        self.ShellCommand = f"shell{Config.CMD_SUFFIX}"
        self.AExecCommand = f"aexec{Config.CMD_SUFFIX}"
        self.ExecCommand = f"exec{Config.CMD_SUFFIX}"
        self.ClearLocalsCommand = f"clearlocals{Config.CMD_SUFFIX}"
        self.BotSetCommand = [f"bsettingz{Config.CMD_SUFFIX}", f"bs2{Config.CMD_SUFFIX}"]
        self.UserSetCommand = [f"usettingz{Config.CMD_SUFFIX}", f"us2{Config.CMD_SUFFIX}"]
        self.SelectCommand = f"selz{Config.CMD_SUFFIX}"
        self.RssCommand = f"rss{Config.CMD_SUFFIX}"


BotCommands = _BotCommands()
