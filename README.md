地理空间数据区块链存证系统

基于区块链技术的地理空间数据存证系统，利用 Sepolia 测试网实现文件哈希存证、时间戳记录和防篡改验证。

一、项目背景

在地理信息系统（GIS）领域，数据来源的可信性和时效性至关重要。本项目通过智能合约将文件哈希上传至以太坊 Sepolia 测试网，利用区块链的不可篡改特性，为地理空间数据提供公开、可验证的存在证明。

二、技术栈

| 类别       | 技术                          |
|------------|-------------------------------|
| 智能合约   | Solidity ^0.8.8               |
| 部署工具   | Remix IDE + MetaMask          |
| 区块链网络 | Sepolia 测试网                |
| 交互脚本   | Python 3 + Web3.py            |
| 节点服务   | Infura                        |
| 版本控制   | Git + GitHub                  |

三环境配置

1. 克隆仓库
   git clone https://github.com/zhanglinguo/geospatial-data-blockchain.git
   cd geospatial-data-blockchain

2.安装依赖
   pip install web3

3. 配置敏感信息（重要）
   在项目根目录创建 config.py 文件（已加入 .gitignore，不会被上传到 GitHub），内容如下：
WEB3_PROVIDER = "https://sepolia.infura.io/v3/你的Infura项目ID"
CONTRACT_ADDRESS = "0x449CBAF621E7b28577530779395C182b1398D725"
PRIVATE_KEY = "你的钱包私钥"   # 注意：不要加 0x 前缀

四、运行测试
1. 上传文件哈希（需消耗 Gas 费）
python upload_hash.py

成功输出示例：
文件哈希：04e97b50852bc83d355ba3a87d963a782714cf1b61783f94dc0054cb59b30
交易已发送，哈希：0x7a2f...
等待确认...
✅ 上链成功！区块高度：10773562

2. 验证文件完整性（免费查询）
python verify_hash.py

输出示例：
✅ 文件哈希已在链上，未被篡改！
上链时间戳：1777736148 (2026-05-02 15:35:48)

五、篡改检测测试
1. 修改 data/elevation_sample.csv 中的任意数据。

2. 再次运行：
python verify_hash.py

预期输出：
❌ 文件哈希未在链上，可能是新文件或已被篡改！

六、 核心合约说明
合约地址：Sepolia Etherscan

函数	类型	说明
storeHash(string memory _hash)	写（需 Gas）	存储文件哈希及当前区块时间戳
getTimestamp(string memory _hash)	读（免费）	查询哈希对应的上链时间
exists(string memory _hash)	读（免费）	检查哈希是否已被存储

七、 项目结构
text
blockchain_verify/
├── config.py               # 敏感配置（不提交）
├── upload_hash.py          # 上传脚本
├── verify_hash.py          # 验证脚本
├── .gitignore              # Git 忽略规则
├── data/
│   └── elevation_sample.csv   # 待存证的数据文件
└── screenshots/            # 运行截图（可选）

八、 未来改进方向
支持批量文件存证

增加前端 Web 界面（React + Web3.js）

集成 IPFS 存储大文件

支持更多区块链网络（如 Polygon、Arbitrum）

九、 许可证
MIT License

联系方式
欢迎交流：GitHub zhanglinguo


