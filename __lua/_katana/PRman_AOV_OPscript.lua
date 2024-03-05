AOVslocation = 'D:/Work/Projects/Project_Dawn/_outputs/02/'
RSO = 'renderSettings.outputs.'
frame = Interface.GetCurrentTime()

--Primary
Interface.SetAttr(RSO..'primary.locationType', StringAttribute("file"))
Interface.SetAttr(RSO..'primary.showMe', IntAttribute(1))
Interface.SetAttr(RSO..'primary.locationSettings.renderLocation', StringAttribute(AOVslocation..'primary.'..frame..'.exr'))

--AOV Function
function AOV(AOVname, AOVsource)
    --PRman Object Channel Define
    Interface.SetAttr('prmanGlobalStatements.outputChannels.'..AOVname..'.name', StringAttribute(AOVname))
    Interface.SetAttr('prmanGlobalStatements.outputChannels.'..AOVname..'.type', StringAttribute("color"))
    --params
    Interface.SetAttr('prmanGlobalStatements.outputChannels.'..AOVname..'.params.source.type', StringAttribute("string"))
    Interface.SetAttr('prmanGlobalStatements.outputChannels.'..AOVname..'.params.source.value', StringAttribute(AOVsource))

    --Render Output Define
    Interface.SetAttr(RSO..''..AOVname..'.rendererSettings.channel', StringAttribute(AOVname))
    Interface.SetAttr(RSO..''..AOVname..'.locationType', StringAttribute("file"))
    Interface.SetAttr(RSO..''..AOVname..'.showMe', IntAttribute(1))
    Interface.SetAttr(RSO..''..AOVname..'.locationSettings.renderLocation', StringAttribute(AOVslocation..AOVname..'/'..AOVname..'.'..frame..'.exr'))
end

--AOVs Create
AOV('diffuse', "lpe:nothruput;noinfinitecheck;noclamp;unoccluded;overwrite;C<.S'passthru'>*((U2L)|O)")
AOV('normal' , "Nn")
AOV('directDiffuse' , "lpe:C<RD>[<L.>O]")
AOV('indirectDiffuse' , "lpe:C<RD>[DS]+[<L.>O]")
AOV('directSpecular' , "lpe:C<RS>[<L.>O]")
AOV('indirectSpecular' , "lpe:C<RS>[DS]+[<L.>O]")
AOV('directSpecularPrimaryLobe' , "lpe:CS2[<L.>O]")
AOV('directSpecularRoughLobe' , "lpe:CS3[<L.>O]")
AOV('directSpecularClearcoatLobe' , "lpe:CS4[<L.>O]")
AOV('indirectSpecularClearcoatLobe' , "lpe:CS4[DS]+[<L.>O]")
AOV('subsurface' , "lpe:CD3[DS]*[<L.>O]")
AOV('transmissiveSingleScatter' , "lpe:CS7[DS]*[<L.>O]")