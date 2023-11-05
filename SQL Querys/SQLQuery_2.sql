BULK INSERT dbo.db0
FROM '/311_Service_Requests_from_2010_to_Present_20231023.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2,
        ROWTERMINATOR = '0x0a',
        FIELDTERMINATOR = ',',
        TABLOCK --Requirement for minimal logging
        --LASTROW = 102
)
GO