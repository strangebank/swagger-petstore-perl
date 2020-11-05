# SearchVideo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sec_item_id** | **str** | 特殊加密的视频id通过用户视频搜索的评论接口获取到 | 
**item_id** | **str** | 视频id | 
**title** | **str** | 视频标题 | 
**cover** | **str** | 视频封面 | 
**is_top** | **bool** | 是否置顶 | 
**create_time** | **int** | 视频创建时间戳 | 
**is_reviewed** | **bool** | 表示是否审核结束。审核通过或者失败都会返回true，审核中返回false。 | 
**share_url** | **str** | 视频播放页面。视频播放页可能会失效，请在观看视频前调用/video/data/获取最新的播放页。 | 
**open_id** | **str** | 作者openID | 
**avatar** | **str** | 头像 | 
**nickname** | **str** | 昵称 | 
**statistics** | [**SearchVideoStatistics**](SearchVideoStatistics.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

